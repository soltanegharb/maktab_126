products = [
 {"name": "Laptop", "price": 150000, "stock": 0},
 {"name": "Mouse", "price": 30000, "stock": 50},
 {"name": "Keyboard", "price": 40000, "stock": 20},
 {"name": "Monitor", "price": 200000, "stock": 10},
]

def my_desired_output(products):
    if isinstance(products,list):
        try:
            filtered = list(filter(lambda product:int(product["price"]) < 50000 and int(product["stock"]) > 0 ,products))
            return filtered
        except:
            return "something went wrong"
    else:
        return f"input must be a list but yours is{str(type(products))[6:-1]}"
print(my_desired_output(products))