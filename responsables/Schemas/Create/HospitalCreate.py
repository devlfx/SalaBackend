from pydantic import BaseModel
from pydantic.networks import EmailStr
from datetime import date, datetime

## Hospital

class HospitalCreate(BaseModel):
    nombre: str
    direccion: str
    telefono :str

    class Config:
        orm_mode = True