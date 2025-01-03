def my_generator():
    yield 'First Value'
    yield 'Second Value'
    yield 'Third Value'

# Accessing the generator
print(list(my_generator()))
gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


