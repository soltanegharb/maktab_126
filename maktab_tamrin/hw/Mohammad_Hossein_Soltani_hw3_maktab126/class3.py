def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    out = fibonacci(n-2)+fibonacci(n-1)
    return out
print(fibonacci(16))