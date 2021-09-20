from typing import List
from fastapi import Depends, HTTPException,Request
from sqlalchemy.orm import Session   
from Database import get_db
from Database.models import models
from responsables.Schemas.Create import EstanciaCreate
from uuid import uuid4
from fastapi_jwt_auth import AuthJWT

class EstanciaController:

    def __init__(self, db:Session = Depends(get_db),AuthJWT:AuthJWT = Depends()):
        self.db = db
        self.auth_jwt = AuthJWT

    async def get_estancias(self):
        self.auth_jwt.jwt_required()
        user_data = self.auth_jwt.get_raw_jwt()
        data = self.db.query(models.Estancia) \
            .filter(models.Estancia.re.any(models.Responsable.id_responsable == user_data.get("id_responsable"))) \
            .all()
        if not data:
            raise HTTPException(status_code=404, detail="Item not found")
        return data

    
    async def get_estancia(self,id_estancia:int):
        self.auth_jwt.jwt_required()
        #self.auth_jwtjwt_optional()
        user_data = self.auth_jwt.get_raw_jwt()
 
        data = self.db.query(models.Estancia) \
            .filter(models.Estancia.re.any(models.Responsable.id_responsable == user_data.get("id_responsable"))) \
            .filter(models.Estancia.id_estancia == id_estancia) \
            .first()
        if not data:
            raise HTTPException(status_code=404, detail="Item not found")
        return data

    async def create_estancia(self,estancia: EstanciaCreate):
        identificador = uuid4()
        data = estancia.dict()
        data['identificador'] = identificador.hex
        db_item = models.Estancia(**data)
        self.db.add(db_item)
        self.db.commit()

        
        


