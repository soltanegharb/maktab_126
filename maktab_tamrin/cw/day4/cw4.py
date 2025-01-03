def log_decorator(func):
    def wrapper(*args,**kwargs):
        print("Starting process_data...")
        result=func(*args,**kwargs)
        print("Finished process_data!")
        return result
    return wrapper

@log_decorator
def do_work():
    print("Working...")

do_work()