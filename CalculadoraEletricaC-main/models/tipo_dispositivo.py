from peewee import AutoField, CharField, Model

from config.database import database


class TipoDispositivoDB(Model):
    id = AutoField()
    nome = CharField()

    class Meta:
        database = database
        table_name = 'tipos_dispositivos'