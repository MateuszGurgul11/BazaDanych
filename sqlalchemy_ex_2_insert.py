from sqlalchemy_ex_1 import students, engine

ins = students.insert().values(name = "siema", lastname = "black")

conn = engine.connect()
result = conn.execute(ins)
conn.execute(ins, [
    {"name": "John", "lastname": "White"},
    {"name": "Martin", "lastname": "Orange"},
    ])