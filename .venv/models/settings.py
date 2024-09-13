from .base import BaseModel
from peewee import CharField

class Contacts(BaseModel):
    phone = CharField()
    email = CharField()
    address = CharField()
    time = CharField()


# last 5 labels
class MainInfo(BaseModel):
    aboutTitle = CharField()


class WhyWeeBlock(BaseModel):
    title = CharField()
    description = CharField()