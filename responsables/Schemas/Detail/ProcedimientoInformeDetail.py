from pydantic import BaseModel
from typing import List, Optional
from .ProcedimientoShow import ProcedimientoShow

class ProcedimientoInformeShow(BaseModel):
    id_procedimiento_informe: int
    id_procedimiento: int
    id_informe: int

    procedimiento: ProcedimientoShow 


    class Config:
        orm_mode = True
