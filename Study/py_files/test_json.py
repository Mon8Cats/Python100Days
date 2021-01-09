import json

userJson = '{"first_name": "John", "last_name":"Doe", "age": 30}'
user = json.loads(userJson)  # Json -> python dictionary
print(user)
print(user["first_name"])


car = {'make': 'Ford', 'model': 'Mustang', 'year': 2020}
carJson = json.dumps(car)
print(carJson)
