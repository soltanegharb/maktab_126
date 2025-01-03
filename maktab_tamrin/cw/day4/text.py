from time import time,sleep
def my_decorator():
    def logger(func):
        print("start")
        def wrapper(*args,**kwargs):
            start = time()
            res = func(*args,**kwargs)
            end = time()
            
            return res
        print(f"finish")
        return wrapper
    return logger
@my_decorator()
def removeCharRecursive(str, X):
    sleep(1)
    # Base Case
    if (len(str) == 0):
        return ""
    
    # Check the first character
    # of the given string
    if (str[0] == X):

        # Pass the rest of the string
        # to recursion Function call
        return removeCharRecursive(str[1:], X)
    
    # Add the first character of str
    # and string from recursion
    return str[0] + removeCharRecursive(str[1:], X)

# Driver Code

# Given String
str = "geeksforgeeks"

# Given character
X = 'e'

# Function call
str = removeCharRecursive(str, X)

print(str)
 