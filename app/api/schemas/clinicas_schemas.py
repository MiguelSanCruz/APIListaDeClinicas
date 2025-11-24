from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from api.services.clinicas_database import Base


class ClinicaModel(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True, index=True)
    clinica = Column(String)
    especialidade = Column(String)
    endereco = Column(String)

class Clinica(BaseModel):
    clinica: str
    especialidade: str
    endereco: str

    model_config = {
        "from_attributes": True
    }

class ClinicaUpdate(BaseModel):
    clinica: str | None = None
    especialidade: str | None = None
    endereco: str | None = None

    model_config = {
        "from_attributes": True
    }