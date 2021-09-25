
from datetime import datetime
from fastapi import Depends, HTTPException,Request,BackgroundTasks
from sqlalchemy.orm import Session   
from Database import get_db
from Database.models import models
from responsables.Schemas.Create import InformeCreate
from responsables.Events.Event import post_event
from responsables.Schemas.Base import ProcedimientoAuthorize
import asyncio
from fastapi_jwt_auth import AuthJWT

class InformeController:

    def __init__(self,background_tasks: BackgroundTasks, db:Session = Depends(get_db),AuthJWT:AuthJWT = Depends()):
        self.db = db
        self.bg_task = background_tasks
        self.auth_jwt = AuthJWT

    async def get_informe(self,id_informe:int):
        data = self.db.query(models.Informe).get(id_informe)
        if not data:
            raise HTTPException(status_code=404, detail="Item not found")
        return data

    async def create_informe(self, inform:InformeCreate):
        data = inform.dict()
        del data["procedimientos"]
        del data["fecha"] # = datetime.now()
        inform_db = models.Informe(**data)
        procedures = [
                models.ProcedimientoInforme(id_procedimiento = proc.id_procedimiento)
                for proc in inform.procedimientos
            ]
        for proc in procedures:
            inform_db.procedimiento_informe.append(proc)
        self.create_notifications_from_inform(inform=inform_db)
        self.db.add(inform_db)
        self.db.commit()
        self.db.refresh(inform_db)
        self.bg_task.add_task(post_event,"inform_created",inform_db)
    
    def create_notifications_from_inform(self, inform: models.Informe):
        estancia = self.db.query(models.Estancia).\
                get(inform.id_estancia)
        
        for responsable in estancia.re:
            notification = models.Notificacion(
                    id_responsable= responsable.id_responsable,
                    active = 1
                )
            inform.notificaciones.append(notification)

    async def authorize_procedure(self,procedureInform : ProcedimientoAuthorize):
        self.auth_jwt.jwt_required()
        user_data = self.auth_jwt.get_raw_jwt()
        prc_inform_db = self.db.query(models.ProcedimientoInforme).filter(models.ProcedimientoInforme.id_procedimiento_informe == procedureInform.id_procedimiento_informe).first()
        if not prc_inform_db:
            raise HTTPException(status_code=404, detail="Item not found")
        if len(prc_inform_db.procedimiento_autorizacion) > 0:
            return 
        informe_db = prc_inform_db.informe
        authorization = models.ProcedimientoAutorizacion(
            id_estancia = informe_db.id_estancia
            , id_responsable = user_data.get("id_responsable")
            , id_procedimiento_informe = prc_inform_db.id_procedimiento_informe
        )
        prc_inform_db.procedimiento_autorizacion.append(authorization)
        self.db.add(prc_inform_db)
        self.db.commit()

