def vorodi(*args):
    print(len(list(args)))
    print(sum(list(args)))
    
def vorodi2(*args,**kwargs):
    print(len(list(args)+list(kwargs)))
    print(sum(list(args)+list(kwargs)))
