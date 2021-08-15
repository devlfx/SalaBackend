from typing import Optional
from pydantic import BaseModel


class DispositivoResponsableBase(BaseModel):
    id_responsable:int
    token_equipo: str
    identifier:Optional[str]
    tipo_equipo:int