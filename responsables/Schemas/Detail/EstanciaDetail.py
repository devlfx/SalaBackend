from typing import List
from responsables.Schemas.Show import EstanciaShow
from .InformeDetail import InformeDetail


class EstanciaDetail(EstanciaShow):
    informes: List[InformeDetail]
    
