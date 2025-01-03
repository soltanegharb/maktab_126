import json
my_dict = {"name": "Alice", "age": 25, "city": "Wonderland"}
json_encoded = json.dumps(my_dict)
print(json_encoded)
json_decoded = json.loads(json_encoded)
print(json_decoded)
