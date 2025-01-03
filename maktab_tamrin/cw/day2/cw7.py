try :
    with open('data.txt','r') as file:
        file.read()
except FileNotFoundError:
    print("File not found!")
