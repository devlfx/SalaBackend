from typing import List, Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr
from datetime import date, datetime


class EstanciaCreate(BaseModel):
    id_paciente: int
    id_hospital: int
    fecha_ingreso: Optional[datetime]
    identificador: Optional[str]

    class Config:
        orm_mode = True