from responsables.Schemas.Base import InformeBase
from typing import List, Optional
from .ProcedimientoInformeCreate import ProcedimientoInformeCreate

class InformeCreate(InformeBase):
    procedimientos: Optional[ List[ ProcedimientoInformeCreate ] ]
    class Config:
        orm_mode = True
