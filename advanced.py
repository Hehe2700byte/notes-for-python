#decorator
def Log_Function(func):
    def wrapper(*args, **kwargs):#wrapper is one type of decorators
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result
    return wrapper

@Log_Function#add(1, 2) is equivalent to Log_Function(add(1, 2))
def add(x, y):
    return x + y

add(1, 2)