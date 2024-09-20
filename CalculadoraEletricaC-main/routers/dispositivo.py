from fastapi import APIRouter, HTTPException
from models.dependencia import DependenciaDB
from models.dispositivo import DispositivoDB
from models.unidade_consumidora import UnidadeConsumidoraDB
from schemas.dispositivos import (
    DispositivoCreate,
    DispositivoRead,
    DispositivoReadList,
    DispositivoUpdate,
)
from utils.erros import (
    unidade_consumidora_not_found_error,
    dependencia_not_found_error,
    dispositivo_not_found_error
)

router = APIRouter(prefix='/dispositivos', tags=['DISPOSITIVOS'])


@router.post('', response_model=DispositivoRead)
def criar_dispositivo(novo_dispositivo: DispositivoCreate):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(
        UnidadeConsumidoraDB.id == novo_dispositivo.unidade_consumidora_id)
    if not unidade_consumidora:
        raise unidade_consumidora_not_found_error()

    dispositivo = DispositivoDB.create(**novo_dispositivo.model_dump())
    return dispositivo


@router.get('/unidades-consumidoras/{unidade_consumidora_id}', response_model=DispositivoReadList)
def listar_dispositivos_por_unidade_consumidora(unidade_consumidora_id: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == unidade_consumidora_id)
    if not unidade_consumidora:
        raise unidade_consumidora_not_found_error()

    dispositivos = DispositivoDB.select().where(DispositivoDB.unidade_consumidora == unidade_consumidora)
    return {'dispositivos': dispositivos}


@router.get('/dependencias/{dependencia_id}', response_model=DispositivoReadList)
def listar_dispositivos_por_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if not dependencia:
        raise dependencia_not_found_error()

    dispositivos = DispositivoDB.select().where(DispositivoDB.dependencia == dependencia)
    return {'dispositivos': dispositivos}


@router.get('/{dispositivo_id}', response_model=DispositivoRead)
def listar_dispositivo(dispositivo_id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    if not dispositivo:
        raise dispositivo_not_found_error()
    return dispositivo


@router.patch('/{dispositivo_id}', response_model=DispositivoRead)
def atualizar_dispositivo(dispositivo_id: int, dispositivo_atualizado: DispositivoUpdate):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    if not dispositivo:
        raise dispositivo_not_found_error()

    dispositivo.nome = dispositivo_atualizado.nome or dispositivo.nome
    dispositivo.consumo = dispositivo_atualizado.consumo or dispositivo.consumo
    dispositivo.uso_diario = dispositivo_atualizado.uso_diario or dispositivo.uso_diario
    dispositivo.tipo_id = dispositivo_atualizado.tipo_id or dispositivo.tipo_id
    dispositivo.save()
    return dispositivo


@router.delete('/{dispositivo_id}', response_model=DispositivoRead)
def excluir_dispositivo(dispositivo_id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    if not dispositivo:
        raise dispositivo_not_found_error()

    dispositivo.delete_instance()
    return dispositivo
