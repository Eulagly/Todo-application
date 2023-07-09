import hashlib

def hash_password(password: str | bytes) -> str:
    password = password.encode() if isinstance(password, str) else password

    hash_object = hashlib.sha512(password)
    return hash_object.hexdigest()
