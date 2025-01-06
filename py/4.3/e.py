def result_accumulator(old_func):
    queue = []

    def new_func(*args, method="accumulate"):
        nonlocal queue
        queue.append(old_func(*args))
        if method == "drop":
            result = queue.copy()
            queue.clear()
            return result

    return new_func