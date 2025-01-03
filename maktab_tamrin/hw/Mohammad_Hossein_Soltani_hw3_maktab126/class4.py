import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        # result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        return "hello"#result
    return wrapper
@timer_decorator
def my_function():
    time.sleep(2)
    return 
print(my_function())