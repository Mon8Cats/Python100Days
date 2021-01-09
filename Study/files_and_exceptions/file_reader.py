filename = "programming2.txt"

title = "Alice in Wonderland"
print(title.split())


'''
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"\nSorry, the file {filename} does not exist.")



print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)



try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")



with open(filename, 'a') as file_obj:
    file_obj.write("I love python\n")



with open(filename) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    # print(line.rstrip())
    #pi_string += line.rstrip()
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))


with open('pi_digits.txt') as file_obj:
    contents = file_obj.read()
print(contents.rstrip())


with open('pi_digits.txt') as file_obj:
    for line in file_obj:
        print(line.rstrip())
'''
