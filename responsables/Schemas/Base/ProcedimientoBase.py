import decimal
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from decimal import *

class ProcedimientoBase(BaseModel):
    nombre: str
    duracion_aproximada: Decimal
    costo: Decimal
    descripcion:str
    class Config:
        orm_mode = True
