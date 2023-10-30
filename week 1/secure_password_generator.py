import secrets


def get_secure_password():
    password = secrets.token_hex(nbytes=32)
    print(password)


get_secure_password()
