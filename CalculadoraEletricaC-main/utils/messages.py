from fastapi import status
from fastapi.responses import JSONResponse


def bandeira_deleted_message():
    return JSONResponse(
        content={'message': 'Bandeira deletada com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )


def dependencia_deleted_message():
    return JSONResponse(
        content={'message': 'Dependencia deletada com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )


def dispositivo_deleted_message():
    return JSONResponse(
        content={'message': 'Dispositivo deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )
def tipo_consumidor_deleted_message():
    return JSONResponse(
        content={'message': 'Tipo de Consumidor deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )
def tipo_dispositivo_deleted_message():
    return JSONResponse(
        content={'message': 'Tipo de Dispositivo deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )
def unidade_consumidora_deleted_message():
    return JSONResponse(
        content={'message': 'Unidade Consumidora deletado com sucesso!'},
        status_code=status.HTTP_202_ACCEPTED,
    )