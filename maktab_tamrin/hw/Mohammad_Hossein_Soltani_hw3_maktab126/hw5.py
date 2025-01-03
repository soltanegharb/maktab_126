def filter_adults(users):
    if isinstance(users,list):
        try:
            filtered = list(filter(lambda person:int(person["age"]) >= 18 , users))
            return filtered
        except:
            return "Sorry 'filter_adults' function had a problem with your input list"
    else:
        return f"Sorry 'filter_adults' function only accepts list but\n is{str(type(users))[6:-1]}"


def convert_names_to_uppercase(users):
    from copy import deepcopy
    if isinstance(users,list):
        try:
            myusers = deepcopy(users)
            myusers = list(map(lambda user:{**user,"name":user["name"].upper()} , myusers))
            # for i in range(len(myusers)):
            #     myusers[i]["name"] = list(map(lambda user:user["name"].upper() , myusers))[i]
            return myusers
        except:
            return "Sorry 'convert_names_to_uppercase' function had a problem with your input list"
    else:
        return f"Sorry 'convert_names_to_uppercase' function only accepts list but\n is{str(type(users))[6:-1]}"


def calculate_average_score(users):
    try:
        ave_score = sum([user["score"] for user in users])
        return ave_score/len(users)
    except:
        return "Something went wrong in 'calculate_average_score' function"
    


def generate_high_score_users(users, min_score):
    # for user in filter(lambda user:user["score"]>min_score,users):
    #     yield user
    return (user for user in filter(lambda user:user["score"]>min_score,users))

# input
users = [
 {"name": "Ali", "age": 25, "score": 85},
 {"name": "Reza", "age": 17, "score": 90},
 {"name": "Sara", "age": 30, "score": 95},
 {"name": "Shima", "age": 22, "score": 70},
 {"name": "Mina", "age": 16, "score": 50},
 {"name": "Hasan", "age": 18, "score": 65},
]
# فیلتر کاربران بالغ 1. 
adults = filter_adults(users)
# تبدیل نامها به حروف بزرگ 2. 
uppercase_users = convert_names_to_uppercase(adults)
print(uppercase_users)

# محاسبه میانگین امتیاز 3. 
average_score = calculate_average_score(uppercase_users)
print(average_score)

# تولید کاربران با امتیاز باال )با ژنراتور ( 4. 
high_score_users = list(generate_high_score_users(uppercase_users, 80))
print(high_score_users)
