from peewee import AutoField, CharField, FloatField, Model

from config.database import database


class TipoConsumidorDB(Model):
    id = AutoField()
    nome = CharField()
    valor_kwh = FloatField()

    class Meta:
        database = database
        table_name = 'tipos_consumidores'