from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ProcedimientoAutorizacionShow(BaseModel):
    id_procedimiento_autorizacion: int
    id_estancia: int
    id_responsable: int
    fecha_autorizacion: datetime
    id_procedimiento_informe: int


    class Config:
        orm_mode = True
