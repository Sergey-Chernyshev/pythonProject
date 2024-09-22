from .base import BaseModel
from peewee import CharField

class Contacts(BaseModel):
    phone = CharField()
    email = CharField()
    address = CharField()
    time = CharField()


class ServicesForTypes(BaseModel):
    title = CharField()


class ServicesTypes(BaseModel):
    title = CharField()
    forTypeId = CharField()

class Services(BaseModel):
    title = CharField()
    fotServiceType = CharField()
