from fastapi import HTTPException, status

def bandeira_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Bandeira não encontrada',
    )

def dependencia_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Dependência não encontrada',
    )

def dispositivo_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Dispositivo não encontrado',
    )

def tipo_consumidor_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Tipo de Consumidor não encontrado',
    )

def tipo_dispositivo_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Tipo de Dispositivo não encontrado',
    )

def unidade_consumidora_not_found_error():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Unidade Consumidora não encontrada',
    )
