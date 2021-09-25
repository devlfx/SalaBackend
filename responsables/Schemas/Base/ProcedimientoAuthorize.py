from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ProcedimientoAuthorize(BaseModel):
    id_procedimiento_informe: int
