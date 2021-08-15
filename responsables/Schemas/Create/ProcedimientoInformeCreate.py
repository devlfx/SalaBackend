from pydantic import BaseModel
from typing import List, Optional


class ProcedimientoInformeCreate(BaseModel):
    id_procedimiento: int
    id_informe: Optional[int]