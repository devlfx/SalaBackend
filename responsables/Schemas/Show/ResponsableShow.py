from typing import List, Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr



class ResponsableShow(BaseModel):
    id_responsable:int
    nombre:str
    apellido_1:str
    apellido_2:str
    email:EmailStr  
    identificador:str

    class Config:
        orm_mode = True