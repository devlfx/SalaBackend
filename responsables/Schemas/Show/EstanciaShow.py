from responsables.Schemas.Create import EstanciaCreate
from .HospitalShow import HospitalShow
from .PacienteShow import PacienteShow

class EstanciaShow(EstanciaCreate):
    id_estancia:int
    hospital: HospitalShow
    paciente: PacienteShow