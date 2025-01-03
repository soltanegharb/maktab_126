with open('cw5.txt','w+') as file:
    file.write('Learning Python is fun!')
    file.seek(0)
    print(file.read())
