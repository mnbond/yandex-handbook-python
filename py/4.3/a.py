def recursive_sum(*numbers):
    if len(numbers) == 0:
        return 0
    return numbers[-1] + recursive_sum(*numbers[:-1])
