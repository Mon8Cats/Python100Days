# creating, reading, updating, deleting files
#

myfile = open('myfile.txt', 'w')
print(f'File name: {myfile.name}')
print(f'Is closed: {myfile.closed}')
print(f'Opening mode: {myfile.mode}')

myfile.write("I love Python")
myfile.write(' and JavaScript')
myfile.close()
print(f'Is closed: {myfile.closed}')
print(f'Opening mode: {myfile.mode}')


myfile = open('myfile.txt', 'a')
myfile.write(' I also like C++')
myfile.close()


myfile = open('myfile.txt', 'r')
print(myfile.read(10))
