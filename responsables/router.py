
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
from responsables.Schemas.Base import ProcedimientoAuthorize
from responsables.Schemas.Auth import UserResponsable
from responsables.Schemas.Show import JWTResponsableShow
from typing import List


router = APIRouter()

# Estancia
@router.get("/estancia/{id_estancia}", status_code=200,response_model=EstanciaDetail,tags=["Autheticated"])
async def get_estancia(id_estancia:int,controller:EstanciaController = Depends(EstanciaController)):
    '''
    Get information about one patient stay, the informs are ordered by data in descendant order.
    '''
    return await controller.get_estancia(id_estancia=id_estancia)


@router.get("/estancia",response_model=List[EstanciaShow],tags=["Autheticated"])
async def get_estancias(controller:EstanciaController = Depends(EstanciaController)):
    '''
    Get a list of la stays of a patient related with a responsible.
    '''
    return await controller.get_estancias()


@router.post("/estancia",status_code=201)
async def create_estancia(estancia:EstanciaCreate,controller:EstanciaController = Depends()):
    '''
    Create a stay for a given patient and hostpital.
    '''
    return await controller.create_estancia(estancia=estancia)


# informe 

@router.get("/inform/{id_informe}", response_model=InformeDetail,tags=["Autheticated"])
async def get_informe(id_informe:int,controller:InformeController = Depends()):
    '''
    Get information of one inform, it includes a list or related procedures.
    '''
    data = await controller.get_informe(id_informe)
    return data 

@router.post("/inform")
async def create_informe(inform:InformeCreate ,controller:InformeController = Depends()):
    '''
    Create an inform with it's related procedures.
    '''
    return await controller.create_informe(inform=inform)

# Procedimientos

@router.post("/procedure/authorization", status_code=200, tags=["Autheticated"])
async def authorize_procedure(procedureInform : ProcedimientoAuthorize, controller:InformeController = Depends()):
    '''
    Create Authorization for a given procedure.
    '''
    return await controller.authorize_procedure(procedureInform = procedureInform)
    



# token

@router.post("/notification/token",status_code=201,tags=["Autheticated"])
async def register_device(device:DispositivoResponsableCreate,controller:DeviceController = Depends()):
    '''
    Register the device token to be able to recieve notifications.
    '''
    return controller.register_device_token(device=device)



# responsable 
@router.post("/responsable",status_code=201,response_model=ResponsableShow)
async def create_resposable(responsable:ResponsableCreate, controller:UserController = Depends()):
    '''
    Create a reponsible, this is equivalent to create a user.
    '''
    data = await controller.create_user(user=responsable)
    return data



# login 

@router.post("/responsable/login",status_code=200,response_model=JWTResponsableShow)
async def login(user:UserResponsable, controller:AuthController = Depends()):
    '''
    Login with a responsible account to have access to the info in the app.
    '''
    return await controller.login(user=user)


# @router.post("responsable/logout")
