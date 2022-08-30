import typer

from pm.database.services import (add_program, get_all_projects, get_program,
                                  get_program_id, get_programs_id,
                                  show_all_programs)

app = typer.Typer()
project_app = typer.Typer()
app.add_typer(project_app, name='project')
program_app = typer.Typer()
app.add_typer(program_app, name='manage')


@project_app.command(name='ls')
def project_ls():
    print("Following projects are in the database:")
    all_p = get_all_projects()
    for p in all_p:
        print(p.name)


@program_app.command(name='add')
def program_add(program_name: str, path: str):
    add_program(program_name, path)
    print(f"Added program {program_name} to database! Hurray!")


@program_app.command(name='delete')
def program_delete(program_name: str):
    program_id = get_programs_id(program_name)
    print(f"Deleted program {program_name} from database! Hurray!")


@program_app.command(name='get')
def program_get(program_name: str):
    program_id = get_program_id(program_name)
    program = get_program(program_id)
    if program:
        print(f"There is a program by the name of {program_id.name}")
    print("No such program in the database")


@program_app.command(name='ls')
def program_ls():
    print("Following programs are installed in the database:")
    all_p = show_all_programs()
    for p in all_p:
        print(p.name)
