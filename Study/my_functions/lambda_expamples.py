def f(a, b): return [
    a,
    b
]


print(f(1, 2))


'''
map( lambda x:
    y=x+1
    z=y-1
    y*z,
    [1, 2, 3])
# expreesson cannot contain assignment


map((lambda x:
     y=x+1
     z=y-1
     y * z,
     [1, 2, 3]))
'''
