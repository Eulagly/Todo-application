import typing
from .load_database import ToDoMysql
from ..Hashing.password import hash_password

def login(db: ToDoMysql, user_login: str, password: str) -> typing.Union[typing.Tuple[bool, int], str]:
    query = "SELECT * FROM user_info WHERE email = %s" if '@' in user_login else "SELECT * FROM user_info WHERE username = %s"
    params = (user_login, )
    db.cursor.execute(query, params)
    row = db.cursor.fetchone()
    if row:
        if row[3] == hash_password(password):
            return True, row[0]
        else:
            return "INVALID_PASSWORD"
    else:
        return "INVALID_USERNAME_OR_EMAIL"

def signup(db: ToDoMysql, email: str, username: str, password: str):
    query = "SELECT * FROM user_info WHERE email = %s"
    params = (email, )
    row = db.cursor.fetchone()
    if row:
        return "ACCOUNT_EMAIL_EXIST"
    else:
        query = "SELECT * FROM user_info WHERE username = %s"
        params = (username, )
        row = db.cursor.fetchone()
        if row:
            return "ACCOUNT_USERNAME_EXIST"
        else:
            query = "INSERT INTO user_info (email, username, password) VALUES (%s, %s, %s)"
            params = (email, username, hash_password(password))
            db.cursor.execute(query, params)

