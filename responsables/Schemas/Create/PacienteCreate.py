from typing import List, Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from datetime import date, datetime


## Paciente
class PacienteCreate(BaseModel):
    identificador: str
    nombre: str
    apellido_1: str
    apellido_2: str

    class Config:
        orm_mode = True
