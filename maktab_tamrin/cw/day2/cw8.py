with open('text.txt','w+') as file:
    file.write('Python is great.\nI love Python programming.')
    for i in file.readlines():
        file.seek(0)
        file.write(i.replace('python','java'))

    print(file.read())
