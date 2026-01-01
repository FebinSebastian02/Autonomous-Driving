# Todo: Basic functions
import numpy
import numpy as np

a, b = 1, 2


def add(num1, num2):  # parameters: variables declared in function's definition
    print(f"Sum: {num1 + num2}")  # print() only shows output
    return num1 + num2  # return sends value back


sum_of_2 = add(a, b)  # arguments: variables passed during function call.
print(sum_of_2)


# Todo: Multiple return values
def math_operations(num1, num2):
    mul_of_2 = num1 * num2
    div_of_2 = num1 / num2
    return mul_of_2, div_of_2


mul_result, div_result = math_operations(a, b)
print(mul_result, div_result)


# Todo: Default arguments
def load_path(path, normalize=True):  # variable normalize is by default True, even if it's value is not passed.
    pass


# Todo: Keyword arguments
load_path(path="data.csv", normalize=False)  # values are assigned to a keyword while passing.


# Todo: Variable number of arguments - *args, **kwargs
def numbers(*args):  # to pass a variable number of non-keyword arguments
    print(args)


numbers(1, 2, "3")


def student_details(**kwargs):  # to pass a variable number of keyword arguments
    print(kwargs)


student_details(name="Febin", age=26, sex="male")


# Todo: Type hints
def compute_speed(distance: float, time: float):  # the data types are assigned to the arguments to improve readability
    print(distance / time)


compute_speed(distance=50.0, time=20.0)


# Todo: Docstrings
def cal_speed(dist, time):
    """This function returns the speed."""
    return dist / time


cal_speed(50, 20)  # Documentation regarding this function obtained by hovering around it.


# Todo: Functions calling functions(modularity)
def normalize(speed):
    return speed / 100


def preprocess(speed):
    return normalize(speed)


preprocessed_speed = preprocess(50)
print(preprocessed_speed)

# Todo: Passing lists/arrays to functions
arr = numpy.array([1, 2, 3])


def scale(array):
    return arr * 2


scaled = scale(arr)
print(scaled)

# Todo: Functions modifying inputs
list1 = [1, 2, 3]


def add_value_to_list(list_of_numbers):
    return list_of_numbers.append(4)  # lists are mutable


add_value_to_list(list1)
print(list1)

# Todo: Lambda functions - short, anonymous functions
square = lambda num: num ** 2  # syntax: lambda argument: expression
print(square(5))

# Todo:Autonomous driving example
speed_cars = [10, 20, 30]


def preprocess_speed(speeds: list):
    speeds = np.array(speeds)
    return speeds / 3.6  # performs element wise division


preprocessed_speeds = preprocess_speed(speed_cars)
print(preprocessed_speeds)


# Todo: Error handling inside functions
def divide_2_num(num1, num2):
    if num2 == 0:  # error
        raise ZeroDivisionError("Division by zero not possible")  # exception handling by giving a meaningful feedback
    return num1 / num2


result = divide_2_num(10, 0)
print(result)
