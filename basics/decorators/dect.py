import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start}")
        return result
    return wrapper

@timer # -> how we declare decorator

def test(n):
    time.sleep(n)

test(2)