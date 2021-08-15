from responsables.Schemas.Show import InformeShow
from responsables.Schemas.Show import ResponsableMedicoShow
from responsables.Schemas.Show import ProcedimientoInformeShow
from typing import List, Optional

class InformeDetail(InformeShow):
    responsable_medico: ResponsableMedicoShow
    procedimiento_informe: Optional [ List [ ProcedimientoInformeShow ] ]

