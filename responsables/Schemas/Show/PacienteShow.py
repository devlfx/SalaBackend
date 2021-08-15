from responsables.Schemas.Create import PacienteCreate


class PacienteShow(PacienteCreate):
    id_paciente: int
    
    