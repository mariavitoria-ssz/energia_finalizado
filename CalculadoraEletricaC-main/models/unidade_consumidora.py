from peewee import AutoField, CharField, ForeignKeyField, Model

from config.database import database
from models.tipo_consumidor import TipoConsumidorDB


class UnidadeConsumidoraDB(Model):
    id = AutoField()
    nome = CharField()
    tipo = ForeignKeyField(
        model=TipoConsumidorDB, backref='unidades_consumidoras'
    )

    class Meta:
        database = database
        table_name = 'unidades_consumidoras'