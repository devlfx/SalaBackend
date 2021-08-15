from pydantic import BaseModel
from typing import List, Optional
from .ProcedimientoShow import ProcedimientoShow
from .ProcedimientoAutorizacionShow import ProcedimientoAutorizacionShow

class ProcedimientoInformeShow(BaseModel):
    id_procedimiento_informe: int
    id_procedimiento: int
    id_informe: int

    procedimiento: ProcedimientoShow 
    procedimiento_autorizacion: Optional [ List [ ProcedimientoAutorizacionShow ] ]

    class Config:
        orm_mode = True
