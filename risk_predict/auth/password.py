import bcrypt


def hash_password(palin_password: str) -> str:

    password_hash: bytes = bcrypt.hashpw(
        palin_password.encode(), bcrypt.gensalt()    
    )
    return password_hash.decode()

def verify_password(
        palin_password: str, password_hash: str
) -> bool:
    return bcrypt.checkpw(
        palin_password.encode(),
        password_hash.encode()    
    )