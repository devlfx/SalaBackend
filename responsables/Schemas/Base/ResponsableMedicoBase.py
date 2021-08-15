from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ResponsableMedicoBase(BaseModel):
    identificador: str
    nombre: str
    apellido_1: str
    apellido_2: str
    id_hospital: int

    class Config:
        orm_mode = True

