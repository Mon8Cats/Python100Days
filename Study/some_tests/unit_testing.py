
mylist = [1, 1, 1, 2, 3, 3, 3, 5, 1, 5, 5, ]
mylist.remove(5)
print(mylist)
mylist.sort(reverse=True)
print(mylist)

"""
Test case:
    run by itself
    determine by itself
    run in isolation

import re

s1 = '100 NORTH BROAD ROAD'
s2 = re.sub('ROAD$', 'RD.', s1)  # $: end with, ^: start with
print(s2)

s1 = "100 BROAD"
s2 = re.sub('ROAD$', 'RD.', s1)
print(s2)
s2 = re.sub('\\bROAD$', 'RD.', s1)
print(s2)
s2 = re.sub(r'\bROAD$', 'RD.', s1)
print(s2)

s1 = "100 BROAD ROAD APT. 3"
s2 = re.sub(r'\bROAD$', 'RD.', s1)
print(s2)
#s2 = re.sub('\bROAD\b', 'RD.', 5)
# print(s2)
"""
