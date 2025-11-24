from fastapi import HTTPException
from api.schemas.clinicas_schemas import Clinica
from api.services.service_factory import get_service

service = get_service()

def listar_clinicas():
    return service.get_all()

def adicionar_clinica(novo: Clinica):
    dados_dict = novo.model_dump()
    return service.post(dados_dict)

def atualizar_clinica(id: int, dados):
    dados_dict = dados.model_dump()
    atualizado = service.update(id, dados_dict)

    if not atualizado:
        raise HTTPException(status_code=404, detail="Clínica não encontrada")

    return atualizado

def remover_clinica(id: int):
    removido = service.delete(id)

    if not removido:
        raise HTTPException(status_code=404, detail="Clínica não encontrada")

    return {"message": "Clínica removida com sucesso"}
