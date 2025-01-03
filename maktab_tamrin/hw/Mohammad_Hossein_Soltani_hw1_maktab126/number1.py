n = int(input('number'))

list_maghsoum = []
for adad in range(1,n//2+1):
    if n % adad == 0:
        list_maghsoum.append(adad)
if sum(list_maghsoum) == n:
    khorouji = '('
    for i in list_maghsoum:
        khorouji += f'{i}'
        if i != list_maghsoum[-1]:
            khorouji += ' + '
    khorouji += f') = {n}'
    print(khorouji)
    print('YES')
else:
    khorouji = '('
    for i in list_maghsoum:
        khorouji += f'{i}'
        if i != list_maghsoum[-1]:
            khorouji += ' + '
    khorouji += f') != {n}'
    print(khorouji)
    print('NO')