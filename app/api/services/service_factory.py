from api.config import MODO_API
from api.services.clinicas_service import ClinicasService
from api.services.clinicas_database import DatabaseService
from api.schemas.clinicas_schemas import ClinicaModel 

def get_service():
    if MODO_API == "internal":
        return ClinicasService()
    return DatabaseService(ClinicaModel)



