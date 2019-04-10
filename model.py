from peewee import *

db = SqliteDatabase('db.sqlite3')


class Domain(Model):
    ip = IPField(unique=True)
    nodes = IntegerField()

    class Meta:
        database = db


class Task(Model):
    domain = ForeignKeyField(Domain, backref='tasks')
    kernel = CharField(max_length=255)
    input = CharField(max_length=255)
    output = CharField(max_length=255, null=True)
    completed = BooleanField(default=False)

    class Meta:
        database = db
