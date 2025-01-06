class CyrillicError(ValueError):
    pass


class CapitalError(ValueError):
    pass


class BadCharacterError(ValueError):
    pass


class StartsWithDigitError(ValueError):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    elif not all(x in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" for x in name.lower()):
        raise CyrillicError
    elif name != name.capitalize():
        raise CapitalError
    return name


def username_validation(username):
    if not isinstance(username, str):
        raise TypeError
    elif not all("a" <= x <= "z" or x == "_" or x.isdigit() for x in username.lower()):
        raise BadCharacterError
    elif username[0].isdigit():
        raise StartsWithDigitError
    return username


def user_validation(**kwargs):
    if set(kwargs) != {"last_name", "first_name", "username"}:
        raise KeyError
    kwargs["last_name"] = name_validation(kwargs["last_name"])
    kwargs["first_name"] = name_validation(kwargs["first_name"])
    kwargs["username"] = username_validation(kwargs["username"])
    return kwargs
