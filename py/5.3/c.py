class Defective:

    def __repr__(self):
        raise Exception


try:
    func(Defective())
except Exception:
    print("Ура! Ошибка!")