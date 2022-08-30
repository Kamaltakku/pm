import datetime

from pony.orm import Optional, Required, Set

from .database import db

Timestamp = datetime.datetime


class Project(db.Entity):
    name: str = Required(str)
    programs = Set('Program')


class Program(db.Entity):
    name: str = Required(str)
    path: str = Required(str)
    date_added: Timestamp = Required(datetime.datetime)
    last_run: Timestamp = Optional(datetime.datetime, nullable=True)
    project: Project = Required(Project)


db.generate_mapping(create_tables=True)
