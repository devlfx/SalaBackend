
from datetime import datetime
from fastapi import Depends, HTTPException,Request
from sqlalchemy.orm import Session   
from Database import get_db
from Database.models import models
from responsables.Schemas.Create import DispositivoResponsableCreate



class DeviceController:
    def __init__(self,db :Session = Depends(get_db)):
        self.db = db

    def register_device_token(self,device:DispositivoResponsableCreate):
        print(device)
        data = device.dict()
        device_db = models.DispositivoResposable(**data)
        self.db.add(device_db)
        self.db.commit()
