n = int(input('number'))
i = 1
while 2 > 1:
    if n < 2 ** i:
        print('NO')
        break
    elif n == 2 ** i:
        print('YES')
        break
    else:
        i+=1