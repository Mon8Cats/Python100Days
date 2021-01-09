'''
**kwargs in function definition:
    it packed the passed named params as dictionary
    this function expect no positinal arguments
    it only takes named arguments

**dictionary in function call
    it unpaked the passed dictionary and assign them mating parms
'''


def named(**kwargs):
    print(kwargs)


def named2(name, age):
    print(name, age)


def print_nicely(**kwargs):
    print("\ninside print_nicely")
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


named(name="Bob", age=25)

details = {"name": "Bob", "age": 25}
named2(**details)

# named(details) # TypeError: named() takes 0 positional arguments but 1 was given
named(**details)  # dictionary --> unpacked --> packed again


print_nicely(**details)
print_nicely(name="tom", age=33)


def both(*args, **kwargs):
    print("\ninside both")
    print(args)  # positonal args --> a tuple
    print(kwargs)  # named args --> a dictionary


both(1, 2, 4, name="Bob", age=25)
