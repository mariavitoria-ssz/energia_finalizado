from peewee import AutoField, CharField, ForeignKeyField, Model

from config.database import database
from models.unidade_consumidora import UnidadeConsumidoraDB


class DependenciaDB(Model):
    id = AutoField()
    nome = CharField()
    unidade_consumidora = ForeignKeyField(
        model=UnidadeConsumidoraDB, backref='dependencias'
    )

    class Meta:
        database = database
        table_name = 'dependencias'