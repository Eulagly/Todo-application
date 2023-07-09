from .load_database import ToDoMysql

class CreateTodo:
    def __init__(self, db: ToDoMysql, owner: int, name: str = "MY_TODO"):
        query = "INSERT INTO todos (name, owner) VALUES (%s, %s)"
        params = (owner, name)
        db.cursor.execute(query, params)

