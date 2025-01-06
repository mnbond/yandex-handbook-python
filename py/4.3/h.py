def fibonacci(n):
    prev, curr = 0, 1
    for i in range(n):
        yield prev
        prev, curr = curr, prev + curr