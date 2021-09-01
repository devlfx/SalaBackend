
from responsables.Schemas.Create.EstanciaCreate import EstanciaCreate
from Database.models.models import Estancia
from fastapi import Depends, HTTPException,APIRouter,Request
from responsables.Controllers.EstanciaController import EstanciaController
from responsables.Controllers.InformeController import InformeController 
from responsables.Controllers.DeviceController import DeviceController
from responsables.Controllers.UserController import UserController
from responsables.Controllers.AuthController import AuthController
from responsables.Schemas.Detail import EstanciaDetail
from responsables.Schemas.Show import EstanciaShow
from responsables.Schemas.Show import ResponsableShow
from responsables.Schemas.Create import EstanciaCreate
from responsables.Schemas.Detail import InformeDetail
from responsables.Schemas.Create import InformeCreate
from responsables.Schemas.Create import DispositivoResponsableCreate
from responsables.Schemas.Create import ResponsableCreate
from responsables.Schemas.Auth import UserResponsable
from responsables.Schemas.Show import JWTResponsableShow
from typing import List


router = APIRouter()

# Estancia
@router.get("/estancia/{id_estancia:int}", status_code=200,response_model=EstanciaDetail,tags=["Autheticated"])
async def get_estancia(id_estancia:int,controller:EstanciaController = Depends(EstanciaController)):
    return await controller.get_estancia(id_estancia=id_estancia)


@router.get("/estancia",response_model=List[EstanciaShow],tags=["Autheticated"])
async def get_estancias(controller:EstanciaController = Depends(EstanciaController)):
    return await controller.get_estancias()


@router.post("/estancia",status_code=201)
async def create_estancia(estancia:EstanciaCreate,controller:EstanciaController = Depends()):
    return await controller.create_estancia(estancia=estancia)


# informe 

@router.get("/inform/{id_informe:int}", response_model=InformeDetail,tags=["Autheticated"])
async def get_informe(id_informe:int,controller:InformeController = Depends()):
    data = await controller.get_informe(id_informe)
    return data 

@router.post("/inform")
async def create_informe(inform:InformeCreate ,controller:InformeController = Depends()):
    return await controller.create_informe(inform=inform)



# token

@router.post("/notification/token",status_code=201,tags=["Autheticated"])
async def register_device(device:DispositivoResponsableCreate,controller:DeviceController = Depends()):
    return controller.register_device_token(device=device)



# responsable 
@router.post("/responsable",status_code=201,response_model=ResponsableShow)
async def create_resposable(responsable:ResponsableCreate, controller:UserController = Depends()):
    data = await controller.create_user(user=responsable)
    return data



# login 

@router.post("/responsable/login",status_code=200,response_model=JWTResponsableShow)
async def login(user:UserResponsable, controller:AuthController = Depends()):
    return await controller.login(user=user)