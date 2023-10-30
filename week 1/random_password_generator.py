# password generator
import random
import string


def random_password_generator():
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(chars, k=24))
    print(password)


random_password_generator()
