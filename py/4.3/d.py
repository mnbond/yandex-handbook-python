def answer(old_func):
    def new_func(*args, **kwargs):
        return f"Результат функции: {old_func(*args, **kwargs)}"
    
    return new_func