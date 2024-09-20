from fastapi import APIRouter, HTTPException
from models.tipo_consumidor import TipoConsumidorDB
from schemas.tipo_consumidor import (
    TipoConsumidorCreate,
    TipoConsumidorRead,
    TipoConsumidorReadList,
    TipoConsumidorUpdate,
)
from utils.erros import tipo_consumidor_not_found_error

router = APIRouter(prefix='/tipos-consumidores', tags=['TIPOS DE CONSUMIDORES'])


@router.post('', response_model=TipoConsumidorRead)
def criar_tipo_de_consumidor(novo_tipo: TipoConsumidorCreate):
    tipo = TipoConsumidorDB.create(**novo_tipo.model_dump())
    return tipo


@router.get('', response_model=TipoConsumidorReadList)
def listar_tipos_de_consumidores():
    tipos = TipoConsumidorDB.select()
    return {'tipos_consumidores': tipos}


@router.get('/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def listar_tipo_de_consumidor(tipo_consumidor_id: int):
    tipo = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    if not tipo:
        raise tipo_consumidor_not_found_error()
    return tipo


@router.patch('/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def atualizar_tipo_de_consumidor(tipo_consumidor_id: int, tipo_atualizado: TipoConsumidorUpdate):
    tipo = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    if not tipo:
        raise tipo_consumidor_not_found_error()

    tipo.nome = tipo_atualizado.nome or tipo.nome
    tipo.valor_kwh = tipo_atualizado.valor_kwh or tipo.valor_kwh
    tipo.save()
    return tipo


@router.delete('/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def excluir_tipo_de_consumidor(tipo_consumidor_id: int):
    tipo = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    if not tipo:
        raise tipo_consumidor_not_found_error()

    tipo.delete_instance()
    return tipo
