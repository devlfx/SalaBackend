from typing import Optional
from pydantic import BaseModel
from datetime import datetime

    # Informes

class InformeBase(BaseModel):
    titulo: str
    descripcion: str
    fecha: Optional[datetime]
    id_estancia: int
    id_responsable_medico:int
    

    class Config:
        orm_mode = True
