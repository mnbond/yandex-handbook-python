def same_type(old_func):
    def new_func(*args):
        if len({type(x) for x in args}) > 1:
            print("Обнаружены различные типы данных")
            return False
        return old_func(*args)
    
    return new_func