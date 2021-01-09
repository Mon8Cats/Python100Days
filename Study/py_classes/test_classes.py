class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def __repr__(self):
        return f"<{self.__class__.__name__} name: {self.name}, email: {self.email}, age: {self.age}>"

    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"

    def has_bithday(self):
        self.age += 1


class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name} and I owe {self.balance}"


john = User("John", "john@mail.com", 22)
print(john)
steve = Customer("Steve", "steve@mail.com", 22)
steve.set_balance(5000)
print(steve)
print(steve.greeting())

'''
steve = User("Steve", "steve@mail.com", 22)
print(steve)
steve.has_bithday()
print(steve)
print(steve.greeting())
'''
