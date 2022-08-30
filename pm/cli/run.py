import typer

from pm.database.services import add_program, delete_program, get_program_id, get_program, show_all_programs, \
    get_programs_id

app = typer.Typer()


@app.command()
def add(program_name: str, path: str):
    add_program(program_name, path)
    print(f"Added program {program_name} to database! Hurray!")


@app.command()
def delete(program_name: str):
    program_id = get_programs_id(program_name)
    print(f"Deleted program {program_name} from database! Hurray!")


@app.command()
def get(program_name: str):
    program_id = get_program_id(program_name)
    program = get_program(program_id)
    if program:
        print(f"There is a program by the name of {program_id.name}")
    print("No such program in the database")


@app.command()
def ls():
    print("Following programs are installed in the database:")
    all_p = show_all_programs()
    for p in all_p:
        print(p.name)