from .base import BaseModel
from pydantic import EmailStr
from peewee import Model, CharField, DateTimeField
from datetime import datetime


class MessagesFromUser(BaseModel):
    phoneNumber = CharField()
    userName = CharField()
    userEmail = CharField(null=True)
    userMessage = CharField(null=True)
    createdAt = DateTimeField(default=datetime.utcnow)
