from fastapi import APIRouter, HTTPException
from models.dependencia import DependenciaDB, UnidadeConsumidoraDB
from schemas.dependencia import (
    DependenciaCreate,
    DependenciaReadList,
    DependenciaReadOne,
    DependenciaUpdate,
)
from utils.erros import dependencia_not_found_error, unidade_consumidora_not_found_error

router = APIRouter(prefix='/dependencias', tags=['DEPENDÊNCIAS'])


@router.post('', response_model=DependenciaReadOne)
def criar_dependencia(novo_dependencia: DependenciaCreate):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(
        UnidadeConsumidoraDB.id == novo_dependencia.unidade_consumidora_id)
    if not unidade_consumidora:
        raise unidade_consumidora_not_found_error()

    dependencia = DependenciaDB.create(**novo_dependencia.model_dump())
    return dependencia


@router.get('/unidade-consumidora/{unidade_consumidora_id}', response_model=DependenciaReadList)
def listar_dependencias_da_unidade_de_consumo(unidade_consumidora_id: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == unidade_consumidora_id)
    if not unidade_consumidora:
        raise unidade_consumidora_not_found_error()

    dependencias = DependenciaDB.select().where(DependenciaDB.unidade_consumidora == unidade_consumidora)
    return {'dependencias': dependencias}


@router.get('/{dependencia_id}', response_model=DependenciaReadOne)
def listar_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if not dependencia:
        raise dependencia_not_found_error()
    return dependencia


@router.patch('/{dependencia_id}', response_model=DependenciaReadOne)
def atualizar_dependencia(dependencia_id: int, novo_dependencia: DependenciaUpdate):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if not dependencia:
        raise dependencia_not_found_error()

    dependencia.nome = novo_dependencia.nome or dependencia.nome
    dependencia.save()
    return dependencia


@router.delete('/{dependencia_id}', response_model=DependenciaReadOne)
def excluir_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if not dependencia:
        raise dependencia_not_found_error()

    dependencia.delete_instance()
    return dependencia
