class BadCharacterError(ValueError):
    pass


class StartsWithDigitError(ValueError):
    pass


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    elif not all("a" <= x <= "z" or x == "_" or x.isdigit() for x in username.lower()):
        raise BadCharacterError
    elif username[0].isdigit():
        raise StartsWithDigitError
    return username
