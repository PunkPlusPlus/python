def memoize(func: callable):
    cache = {}

    def wrapper(*args):
        nonlocal cache
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


def counter(start=0, step=1):
    count = start

    def increment():
        nonlocal count
        count += step
        return count
    return increment
