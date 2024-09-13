from peewee import *
import os

db = SqliteDatabase(os.getenv('DATABASE_URL', 'my_database.db'))

class BaseModel(Model):
    class Meta:
        database = db
