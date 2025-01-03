s = 'listen'
t = 'silent'
c=0
if len(s) == len(t):
    for i in s:
        if i in t:
            c+=1
        elif i not in t:
            print(False)
            break
    if c == len(s):
        print(True)
else:
    print(False)

