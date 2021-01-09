# Unpacking arguments

def multiplyX(*args):
    print(args)


def add(x, y):
    return x + y


nums = [3, 5]
multiplyX(nums)
multiplyX(nums, 9, 10)
multiplyX(*nums)
multiplyX(1, *nums, 9, 10)
print(add(*nums))
# print(add(nums)) # TypeError
print(add(x=3, y=5))

nums_d = {'x': 15, 'y': 25}
print(add(nums_d['x'], nums_d['y']))
print(add(x=nums_d['x'], y=nums_d['y']))
print(add(**nums_d))


'''
*args in function definition: multiple arguments collected into one touple
*tuple in function call: a tuple is unpacked into muliple params
'''

def multiply(*args):
    #print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


def sum(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total


def apply(*args, operator):  # multiple argument collected in one tuple
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(*args)
    else:
        return "No valid operator provided to apply()"


print(apply(7, 2, 4, 5, operator="+"))  # operator is needed


