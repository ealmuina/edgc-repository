from peewee import *

db = SqliteDatabase('db.sqlite3')


class Domain(Model):
    ip = IPField(unique=True)
    nodes = IntegerField()
    cpus = IntegerField()
    mhz = FloatField()
    memory = IntegerField()
    net_speed = IntegerField()

    class Meta:
        database = db


class Task(Model):
    domain = ForeignKeyField(Domain, backref='tasks', null=True)
    cpu_intensity = IntegerField()
    com_intensity = IntegerField()
    mem_intensity = IntegerField()
    kernel = CharField(max_length=255)
    input = CharField(max_length=255)
    output = CharField(max_length=255)
    pack = CharField(max_length=255)
    unpack = CharField(max_length=255)
    completed = BooleanField(default=False)

    class Meta:
        database = db
