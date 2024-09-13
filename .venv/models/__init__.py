from .base import db
from .admin import Admin
from .message import MessagesFromUser



def initialize_db():
    with db:
        db.create_tables([Admin, MessagesFromUser])
