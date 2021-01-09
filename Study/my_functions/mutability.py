a = []
b = a # same object

print(f"is same id? {id(a) == id(b)}")
#print(id(b))

a.append(35)
print(f'a= {a}, b= {b}')


a = []
b = []
print(f"is same id? {id(a) == id(b)}")
#print(id(b))

a = 1234
b = 1234
print(f"is same id? {id(a) == id(b)}")

a = 1235
print(f"is same id? {id(a) == id(b)}")

a = "Hello"
b = a
print(f"is same id? {id(a) == id(b)}")


a += " world"
print(f"is same id? {id(a) == id(b)}")

# immutable ?