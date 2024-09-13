from .base import BaseModel
from peewee import CharField
from passlib.hash import bcrypt

class Admin(BaseModel):
    username = CharField(unique=True)
    password_hash = CharField()

    @classmethod
    def create_admin(cls, username, password):
        password_hash = bcrypt.hash(password)
        return cls.create(username=username, password_hash=password_hash)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)
