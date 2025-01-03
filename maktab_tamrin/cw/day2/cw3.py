file = open('cw3.txt','r')
c=0
for line in file:
    c+=1
print(c)
print(type(file))

file.seek(0)
print(len(file.readlines()))
file.close()
