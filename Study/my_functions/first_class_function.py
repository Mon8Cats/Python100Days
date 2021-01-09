from operator import itemgetter


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend/divisor


def calculate(*values, operator):
    return operator(*values)


#esult = calculate(20, 4, operator=divide)
# print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Steve Kim", "age": 25},
    {"name": "Adam Wool", "age": 35},
    {"name": "Ann Pul", "age": 27},
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Steve Kim", get_friend_name))
print(search(friends, "Adam Wool", lambda friend: friend["name"]))
print(search(friends, "Adam Wool", itemgetter("name")))
