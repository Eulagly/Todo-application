import hashlib

def hash_password(password: str | bytes):
    if type(password) == str:
        password = password.encode()

    hash_password = hashlib.sha512(password)
    hash_password.update(password)
    return hash_password.hexdigest()