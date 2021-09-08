from typing import List
from responsables.Schemas.Show import EstanciaShow
from responsables.Schemas.Detail import InformeDetail


class EstanciaDetail(EstanciaShow):
    informes: List[InformeDetail]
    
