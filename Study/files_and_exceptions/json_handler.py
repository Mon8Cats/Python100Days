import json


'''
def greet_user():
    """Greet the user by name."""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("\nWhat is your name?")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"\nWe'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
'''


def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("\nWhat is your name?")
    filename = "username.json"
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"\nWe'll remember you when you come back, {username}!")

        '''
        username = input("\nWhat is your name?")
        filename = "username.json"
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"\nWe'll remember you when you come back, {username}!")
        '''


greet_user()


'''
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers2 = json.load(f)

print(numbers2)
'''
