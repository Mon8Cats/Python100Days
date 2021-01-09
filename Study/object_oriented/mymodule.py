def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend/divisor


mymoduleName = __name__

if __name__ == "__main__":
    print("mymodule.py: ", __name__)
    # print(mymoduleName)

# divide(5, 0)
# print(divide(5, 0))

grades = [1, 2, 3, 4]
#average = None
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError:
    print("There are no grades yet in your list.")

print(f"The average grade is {average}")
