from hashlib import sha256


class MinLengthError(ValueError):
    pass


class PossibleCharError(ValueError):
    pass


class NeedCharError(ValueError):
    pass


def password_validation(password, min_length=8, 
                        possible_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 
                        at_least_one=str.isdigit):
    if not isinstance(password, str):
        raise TypeError
    elif len(password) < min_length:
        raise MinLengthError
    elif not all(x in possible_chars for x in password):
        raise PossibleCharError
    elif not any(at_least_one(x) for x in password):
        raise NeedCharError
    return sha256(password.encode("utf-8")).hexdigest()