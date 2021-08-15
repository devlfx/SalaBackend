from typing import Optional
from pydantic import BaseModel


class DispositivoResponsableCreate(BaseModel):
    id_responsable:Optional[int]
    token_equipo: str
    identifier:Optional[str]
    tipo_equipo:int