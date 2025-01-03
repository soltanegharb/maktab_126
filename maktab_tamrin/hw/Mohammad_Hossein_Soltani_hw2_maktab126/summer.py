def summer(*args,**kwargs):
    return sum([*args,*kwargs.values()])

print(summer(1,2,3,j=4))