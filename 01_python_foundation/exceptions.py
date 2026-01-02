# Todo: Exception: Python's way of saying - something went wrong at run time, and it doesn't know how to continue unless
#  we handle it.

# x = 10 / 0  # python stops the program immediately unless we handle it.

# Todo: Basic exception handling using try and except
# syntax: try - risky code, except - what to do if it fails.
try:
    speed = int(input("Enter speed"))
    print(100 / speed)  # if speed = 0, python stops the program
except ZeroDivisionError:
    print("Speed cannot be 0")  # here, a meaningful message is given and the program doesn't crash

# Todo: Handling multiple exceptions
try:
    speed = int(input("Enter speed..."))
    print(100 / speed)
except ZeroDivisionError:
    print("Speed cannot be zero")
except ValueError:  # user enters abc
    print("Please enter a number")

# Todo: Catching all exceptions
try:
    risky_code()  # function not defined.
except Exception as exc:  # here, we are trying to catch the possible exception as we don't know the exact exception.
    print("Something went wrong:", exc)

# Todo: Finally block. Finally always runs even when there is error or not. For clean up.
try:
    load = open("data.txt")
    content = load.read()
except FileNotFoundError:
    print("File not found")
finally:
    print(
        "Closing resources...")  # if error - both except and finally block works, no error -  only finally block works.

# Todo: Raising Exceptions
