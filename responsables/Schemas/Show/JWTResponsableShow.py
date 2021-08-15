from typing import List, Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from .ResponsableShow import ResponsableShow

class JWTResponsableShow(BaseModel):
    token:str
    user:ResponsableShow

    class Config:
        orm_mode = True