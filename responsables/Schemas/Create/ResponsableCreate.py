from typing import List, Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from datetime import date, datetime


class ResponsableCreate(BaseModel):
    nombre:str
    apellido_1:str
    apellido_2:str
    email:EmailStr
    password:str
    identificador:str

    class Config:
        orm_mode = True