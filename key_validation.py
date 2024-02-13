class InvalidKeyError(Exception):
    pass
def validate_key(key, filename):
    if key <= 0:
        raise InvalidKeyError("Key must be a positive integer")