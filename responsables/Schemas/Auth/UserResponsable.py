from typing import Optional
from pydantic import BaseModel
from pydantic.networks import EmailStr

class UserResponsable(BaseModel):
    email:EmailStr
    password:str