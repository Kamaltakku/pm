from pony.orm import Database

db = Database()
db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)
