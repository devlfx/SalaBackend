from datetime import datetime
from fastapi import Depends, HTTPException,Request
from sqlalchemy.orm import Session   
from Database import get_db
from Database.models import models
from responsables.Schemas import Auth
from responsables.Schemas.Auth import UserResponsable
from responsables.Schemas.Show import JWTResponsableShow
from responsables.Services.HashService import get_password_hash, verify_password
from fastapi_jwt_auth import AuthJWT

class AuthController:
    def __init__(self, db:Session = Depends(get_db), AuthJWT:AuthJWT = Depends()):
        self.auth_jwt = AuthJWT
        self.db = db



    async def login(self,user:UserResponsable):
        responsable = self.db.query(models.Responsable).filter(models.Responsable.email == user.email).first()
        if not responsable:
            raise HTTPException(status_code=404, detail="Item not found")
        if not verify_password(user.password,responsable.password):
            raise HTTPException(status_code=403,detail="Invalid Credentials")
        data = responsable._asdict()
        del data["password"]
        access_token = self.auth_jwt.create_access_token(subject=responsable.id_responsable,user_claims=data,expires_time=False)
        jti = self.auth_jwt.get_raw_jwt(access_token)['jti']
        token = models.AuthResponsableToken(token = access_token, status = 1,jti = jti)
        responsable.tokens.append(token)
        self.db.add(responsable)
        self.db.commit()
        response = JWTResponsableShow(token=access_token,user=responsable)
        return response



