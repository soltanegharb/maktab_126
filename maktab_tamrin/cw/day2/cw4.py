def zdivision(a,b):
    try :
        return a/b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        
