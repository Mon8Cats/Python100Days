x = 8
y = 6

if x == y:
    print(f'{x} == {y}')
elif x > y:
    print(f'{x} > {y}')
elif x < y:
    print(f'{x} < {y}')
else:
    print(f'{x} != {y}')

if x > 2 or x < 10:
    print(f'{x} is less than 2 or greater than 10')

nubmers = [1, 2, 3, 4, 5]

if x in nubmers:
    print(f'{x} is in the numbers')
else:
    print(f'{x} is not in the numbers')


if x is y:
    print(f'x is y: {x is y}')
else:
    print(f'x is not y: {x is not y}')
