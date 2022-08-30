import datetime

from pony.orm import Required, Optional
from .database import db


class Program(db.Entity):
    name: str = Required(str)
    path: str = Required(str)
    date_added: datetime.datetime = Required(datetime.datetime)
    last_run: datetime.datetime = Optional(datetime.datetime, nullable=True)


db.generate_mapping(create_tables=True)
