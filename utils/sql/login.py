from . import load_database
import typing

def login(db: load_database.ToDoMysql, user_login: str, password: str) -> typing.Tuple[bool, int]:

    query = "SELECT * FROM user_info WHERE email = %s" if '@' in user_login else "SELECT * FROM user_info WHERE username = %s"
    params = (password, )
    db.cursor.execute(query, params)
    if db.cursor:
        row =  db.cursor.fetchone()
        if row[3] == password:
            return (True, row[0])
        else:
            return "INVALID_PASSWORD"
    else:
        return "INVALID_USERNAME_OR_EMAIL"