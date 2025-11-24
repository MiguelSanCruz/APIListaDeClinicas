from fastapi import APIRouter
from api.controllers.clinicas_controller import (
    listar_clinicas,
    adicionar_clinica,
    atualizar_clinica,
    remover_clinica
)
from api.schemas.clinicas_schemas import Clinica , ClinicaUpdate


router = APIRouter()


@router.get("/")
def get_all():
    return listar_clinicas()

@router.post("/")
def post(novo: Clinica):
    return adicionar_clinica(novo)

@router.put("/{id}")
def update(id : int, dados: ClinicaUpdate):
    return atualizar_clinica(id, dados)

@router.delete("/{id}")
def delete(id: int):
    return remover_clinica(id)

