from datetime import datetime
from fastapi import Depends, HTTPException,Request
from sqlalchemy.orm import Session   
from Database import get_db
from Database.models import models
from responsables.Schemas.Create import ResponsableCreate
from responsables.Services.HashService import get_password_hash
from fastapi_jwt_auth import AuthJWT

class UserController:

    def __init__(self, db:Session = Depends(get_db),AuthJWT:AuthJWT = Depends()):
        self.db = db
        self.auth_jwt = AuthJWT

    async def create_user(self,user:ResponsableCreate):
        data = user.dict()
        data["password"] = get_password_hash(data.get("password"))
        user_db = models.Responsable(**data)
        self.db.add(user_db)
        self.db.commit()
        self.db.refresh(user_db)
        return user_db

    async def associate_patient():
        pass