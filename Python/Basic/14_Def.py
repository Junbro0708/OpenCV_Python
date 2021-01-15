def add(*args):
    results = 0
    for i in args:
        results += i
    return results


print(add(1, 2, 3, 4, 5, 6, 7, 8))
