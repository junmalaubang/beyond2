def add(*args):
    total = 0
    for arg in args:
        total = arg + total
    return total


print(add(1, 2, 3, 4, 5))
