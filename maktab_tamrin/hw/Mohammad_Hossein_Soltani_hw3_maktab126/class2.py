def mydecorator(func):
    def wrapper(*args,**kwargs):
        try:
            result = func(*args,**kwargs)
            return "ok"
        except ValueError:
            return "ok"
    return wrapper
@mydecorator
def error_for_3(num):
    if num == 3:
        raise ValueError("number must not be 3")
    return num
print(error_for_3(5))