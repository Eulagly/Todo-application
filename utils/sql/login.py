import typing
from .load_database import ToDoMysql

def login(db: ToDoMysql, user_login: str, password: str) -> typing.Union[typing.Tuple[bool, int], str]:
    query = "SELECT * FROM user_info WHERE email = %s" if '@' in user_login else "SELECT * FROM user_info WHERE username = %s"
    params = (user_login, )
    db.cursor.execute(query, params)
    row = db.cursor.fetchone()
    if row:
        if row[3] == password:
            return True, row[0]
        else:
            return "INVALID_PASSWORD"
    else:
        return "INVALID_USERNAME_OR_EMAIL"