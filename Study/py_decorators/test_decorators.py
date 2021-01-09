
import random
from sk_decorators import (
    PLUGINS,
    # make_secure
    timer,
    debug,
    register,
    slow_down,
    count_calls,
    CountCalls,
    slow_down,
    singleton,
    cache,
    set_unit,
    use_unit
)
# import functools
import math


@use_unit("meters per second")
def average_speed(distance, duration):
    return distance / duration


bolt = average_speed(100, 9.58)
print(bolt)
print(bolt.to("km per hour"))
print(bolt.to("mph").m)


'''
@set_unit("cm^3")
def volumn(radious, height):
    return math.pi * radious**2 * height


print(f"{volumn(3, 5)} {volumn.unit}")


# @cache
# @count_calls
@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calcularing finbonacci({num})")
    if num < 2:
        return num
    return fibonacci(num-1) + fibonacci(num - 2)


print(fibonacci(10))
# print(fibonacci.num_calls)
print(fibonacci(9))
print(fibonacci(5))



@singleton
class TheOne:
    pass


first_one = TheOne()
another_one = TheOne()

print(f"is the same id? {id(first_one) == id(another_one)}")


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


waste_some_time(1)
waste_some_time(99)


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} alreay, you are growing up!"


make_greeting("Ben", 7)
make_greeting("Tom")


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child  # return a reference to the funciton
    else:
        return second_child


first = parent(1)
second = parent(2)
print(f'the first function def: {first}, call: {first()}')
print(f'the second function def: {second}, call: {second()}')


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greeting(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"\nUsing {greeter!r}")
    return greeter_func(name)


print(randomly_greeting('Steve'))


# @slow_down(rate=2)
@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff")
    else:
        print(from_number)
        countdown(from_number-1)


countdown(3)


@count_calls
def say_whee():
    print("Whee!")


say_whee()
say_whee()
print(say_whee.num_calls)


@CountCalls
def say_whee2():
    print("whee!")


say_whee2()
say_whee2()
print(say_whee2.num_calls)

'''
