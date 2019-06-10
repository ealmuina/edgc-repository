from peewee import *

db = SqliteDatabase('db.sqlite3')


class Domain(Model):
    ip = IPField(unique=True)
    nodes = IntegerField()
    cpus = IntegerField()
    mflops = FloatField()
    memory = IntegerField()
    mpi_bandwidth = FloatField()

    class Meta:
        database = db


class Task(Model):
    domain = ForeignKeyField(Domain, backref='tasks', null=True)
    assign_date = DateTimeField(null=True)
    completed_date = DateTimeField(null=True)
    cpu_intensity = IntegerField()
    com_intensity = IntegerField()
    mem_intensity = IntegerField()
    kernel = CharField(max_length=255)
    parameters = CharField(max_length=1023, default='')
    input = CharField(max_length=255, default='')
    output = CharField(max_length=255)
    pack = CharField(max_length=255)
    unpack = CharField(max_length=255)
    completed = BooleanField(default=False)

    class Meta:
        database = db
