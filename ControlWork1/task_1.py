from functools import wraps

def count_calls(func):
    counts = {func.__name__: 0}

    @wraps(func)
    def wrapper(*args, **kwargs):
        counts[func.__name__] += 1
        return func(*args, **kwargs)

    wrapper.counts = counts
    return wrapper

@count_calls
def ru():
    print("Привет!")

@count_calls
def eu():
    print("Hi!")\

@count_calls
def ar():
    print("مرحبًا")

@count_calls
def ja():
    print("こんにちは")


ru()
ru()
eu()
eu()
ar()
ja()
print(ru.counts)
print(eu.counts)
print(ar.counts)
print(ja.counts)