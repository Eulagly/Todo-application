import typing
from .load_database import ToDoMysql
from ..Verification.password import hash_password

def login(db: ToDoMysql, user_login: str, password: str) -> typing.Union[typing.Tuple[bool, int], str]:
    """Check the login credentials against the user database.

    Args:
        db (ToDoMysql): The ToDoMysql instance for database connection.
        user_login (str): The username or email entered by the user.
        password (str): The password entered by the user.

    Returns:
        Union[Tuple[bool, int], str]: If the login is successful, returns a tuple of True and user ID.
                                      If the credentials are invalid, returns an appropriate error message.
    """
    query = "SELECT * FROM user_info WHERE email = %s OR username = %s"
    params = (user_login, user_login)
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
    """Create a new user account in the database.

    Args:
        db (ToDoMysql): The ToDoMysql instance for database connection.
        email (str): The email entered by the user.
        username (str): The username entered by the user.
        password (str): The password entered by the user.

    Returns:
        int or str: If the signup is successful, returns the last inserted ID.
                    If the email or username is already taken, returns an appropriate error message.
    """
    query_check_email = "SELECT * FROM user_info WHERE email = %s"
    params_check_email = (email,)
    db.cursor.execute(query_check_email, params_check_email)
    row_email = db.cursor.fetchone()

    if row_email:
        return "EMAIL_TAKEN"

    query_check_username = "SELECT * FROM user_info WHERE username = %s"
    params_check_username = (username,)
    db.cursor.execute(query_check_username, params_check_username)
    row_username = db.cursor.fetchone()

    if row_username:
        return "USERNAME_TAKEN"

    query_insert = "INSERT INTO user_info (email, username, password) VALUES (%s, %s, %s)"
    params_insert = (email, username, hash_password(password))
    db.cursor.execute(query_insert, params_insert)
    db.connector.commit()

    last_inserted_id = db.cursor.lastrowid
    return last_inserted_id
