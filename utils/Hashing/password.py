import hashlib

def hash_password(password: str | bytes):
    if type(password) == str:
        password = password.encode()

    hash_password = hashlib.sha256()
    hash_password.update(b"Nobody inspects")
    hash_password.update(b" the spammish repetition")
    return hash_password.digest()