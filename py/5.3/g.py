class CyrillicError(ValueError):
    pass


class CapitalError(ValueError):
    pass


def name_validation(name):
    if not isinstance(name, str):
        raise TypeError
    elif not all(x in "абвгдеёжзийклмнопрстуфхцчшщьыъэюя" for x in name.lower()):
        raise CyrillicError
    elif name != name.capitalize():
        raise CapitalError
    return name
