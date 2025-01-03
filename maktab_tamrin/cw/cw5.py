n = int(input('number\n'))

for i in range(1,n+1):
    if i % 15 == 0:
        print('\nFizzBuzz')
    elif i % 3 == 0:
        print('\nFizz')
    elif i % 5 == 0:
        print('\nBuzz')
    else:
        print()
        print(i)
        
