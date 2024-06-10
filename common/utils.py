import hashlib
import random
import secrets
import string


def make_secret(keyword: str):
    """
    Generate a random secret token, everytime you call it wit same keyword
    """
    return hashlib.sha256(
        "{}-{}".format(str(random.getrandbits(256)), keyword).encode("utf-8")
    ).hexdigest()


def make_password(keyword: str):
    """
    convert the keyword into hashed_keyword
    - using the sha256 hash Algo
    """
    return hashlib.sha256("{}".format(keyword).encode()).hexdigest()


def random_chars(length: int):
    """
    this will create a random characters of uppercase and digits mixed
    currently using for:
    1. creating temporary password
    2. creating product code of 7 characters
    """
    raw_chars = [ch for ch in string.ascii_uppercase] + [num for num in string.digits]
    random_characters = "".join(random.choices(raw_chars, k=length))
    return random_characters


def generate_verification_code(length: int = 6) -> str:
    """
    Generates a verification code of the specified length.
    Returns a string representation of the code.
    The secrets module is generally considered to be more
    secure than random because it uses a cryptographically secure
    source of randomness.
    """
    return str(secrets.randbelow(10**length)).zfill(length)
