from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ProcedimientoInformeBase(BaseModel):
    id_informe: int
    id_procedimiento: int

    class Config:
        orm_mode = True
