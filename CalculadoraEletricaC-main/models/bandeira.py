from peewee import AutoField, CharField, FloatField, Model

from config.database import database


class BandeiraDB(Model):
    id = AutoField()
    nome = CharField()
    tarifa = FloatField()

    class Meta:
        database = database
        table_name = 'bandeiras'