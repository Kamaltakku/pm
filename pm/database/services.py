import datetime

from pony.orm import db_session, select

from .models import Program, Project


@db_session
def add_program(name: str, path: str):
    Program(name=name, path=path, date_added=datetime.datetime.now())


@db_session
def get_program(program_id: int):
    return Program[program_id]


@db_session
def show_all_programs():
    return select(p for p in Program)[:]


@db_session
def delete_program(program_id: int):
    Program[program_id].delete()


@db_session
def get_program_id(name: str):
    return Program.get(lambda p: p.name == name)


@db_session
def get_programs_id(name: str):
    programs = Program.select(lambda p: p.name == name)[:]
    print(programs)


@db_session
def delete_more(query_object):
    pass


@db_session
def get_all_projects():
    return select(pr for pr in Project)[:]
