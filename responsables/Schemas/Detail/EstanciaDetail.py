from typing import List
from responsables.Schemas.Show import EstanciaShow
from responsables.Schemas.Show import InformeShow


class EstanciaDetail(EstanciaShow):
    informes: List[InformeShow]
    
