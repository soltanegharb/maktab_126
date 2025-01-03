people = [
 {"name": "Ali", "age": 16},
 {"name": "Reza", "age": 20},
 {"name": "Shima", "age": 25},
 {"name": "Sara", "age": 15},
]
def my_desired_output(people):
    if isinstance(people,list):
        try:
            filtered = list(filter(lambda person:int(person["age"]) > 18 , people))
            mapped = list(map(lambda person:f"{person["name"]}({person["age"]})",filtered))
            return mapped
        except:
            return "Sorry Please check your input list"
    else:
        return f"Sorry wrong input format must be a list but\n is{str(type(people))[6:-1]}"
    
print(my_desired_output(people))