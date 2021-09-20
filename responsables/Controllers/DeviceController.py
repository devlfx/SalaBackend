
from datetime import datetime
from fastapi import Depends, HTTPException,Request
from sqlalchemy.orm import Session   
from Database import get_db
from Database.models import models
from responsables.Schemas.Create import DispositivoResponsableCreate
from fastapi_jwt_auth import AuthJWT


class DeviceController:
    def __init__(self, db:Session = Depends(get_db),AuthJWT:AuthJWT = Depends()):
        self.db = db
        self.auth_jwt = AuthJWT

    def register_device_token(self,device:DispositivoResponsableCreate):
        self.auth_jwt.jwt_required()
        user_data = self.auth_jwt.get_raw_jwt()
        data = device.dict()
        data["id_responsable"] = user_data["id_responsable"]
        db_token =  self.db.query(models.DispositivoResposable).filter(models.DispositivoResposable.id_responsable==user_data["id_responsable"]) \
        .filter(models.DispositivoResposable.token_equipo == data["token_equipo"]).first()
        if not db_token:
            print("nuevo token")
            device_db = models.DispositivoResposable(**data)
            self.db.add(device_db)
            self.db.commit()
        
