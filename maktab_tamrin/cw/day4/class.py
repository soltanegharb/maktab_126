# def mylogger(func):
#     def wrapper(*args,**kwargs):
#         lst , out = func(*args,**kwargs)
#         print(f"number of input list = {len(lst)}\nthe input itself = {lst}")
#         print(f"number of output list = {len(out)}\nthe output itself = {out}")
#     return wrapper

# @mylogger
# def people(lst):
#     out = list(set(lst))
#     return lst , out

# people(["ali","reza","ali","sara","mahmoud","sara"])


def mylogger2(func):
    def wrapper(*args,**kwargs):
        
        print(f"number of input list = {len(*args)}\nthe input itself = {args[0]}")

        out = func(*args,**kwargs)
        print(f"number of output list = {len(out)}\nthe output itself = {out}")
    return wrapper

@mylogger2
def people2(lst):
    out = list(set(lst))
    return out

people2(["ali","reza","ali","sara","mahmoud","sara"])