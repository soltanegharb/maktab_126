def file_reader(file_name):
    try:
        with open(file_name,'r') as f:
            output = f.read()
            #print(output)
            return output
    except FileNotFoundError:
        with open(file_name,'w') as f:
            f.write('Hello, world!\n')
            print('A new file created')

print(file_reader('test.txt'))
#file_reader('test1.txt')