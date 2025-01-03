students = [
 {"name": "Ali", "grade": 18},
 {"name": "Reza", "grade": 15},
 {"name": "Shima", "grade": 19},
 {"name": "Sara", "grade": 14},
]

def my_desired_output(students):
    if isinstance(students,list):
        try:    
            mapped = [x  for x in (map(lambda student:student["name"] if int(student["grade"]) > 17 else None ,students)) if x is not None]
            return mapped
        except:
            return "Something went wrong in your input please recheck it"
    else:
        return f"Sorry please recheck your your input it must be list\nbut yours is{str(type(students))[6:-1]}"
print(my_desired_output(students))