from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from config.database import shutdown_db, startup_db
from routers.bandeira import router as bandeira_router
from routers.dependencia import router as comodo_router
from routers.dispositivo import router as dispositivos_router
from routers.tipo_consumidor import router as tipo_router
from routers.tipo_dispositivo import router as tipo_dispositivos_router
from routers.unidade_consumidora import router as consumidor_router

app = FastAPI(title='CALCULADORA DE CONSUMO DE ENERGIA ELÉTRICA')

app.add_event_handler(event_type='startup', func=startup_db)
app.add_event_handler(event_type='shutdown', func=shutdown_db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def status():
    return {
        'status': 'ok',
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

app.include_router(tipo_router)
app.include_router(consumidor_router)
app.include_router(comodo_router)
app.include_router(tipo_dispositivos_router)
app.include_router(dispositivos_router)
app.include_router(bandeira_router)