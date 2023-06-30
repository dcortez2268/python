"""
FUNCTIONS
"""

""" 
syntax to define function 
"""


def name_of_function(args):
    x = 1
    return x


""" 
map function 
"""


# allows you to call a function on each element of an iterable object and return result of function
def square(num):
    return num**2


my_nums = [1, 2, 3, 4]
my_squared_nums = map(square, my_nums)

""" 
filter function 
"""


# allows you to call a function on each element of an iterable object and returns the elements for which the function returns true
def check_even(num):
    return num % 2 == 0


my_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = filter(check_even, my_nums)

"""
LAMBDA EXPRESSIONS
"""


# anonymous functions
# useful for map, filter functions
# syntax is:  lambda params : value to return
def mult(num1, num2):
    return num1 * num2


# is same as
lambda num1, num2: num1 * num2

"""
*ARGS AND **KWARGS FUNCTION ARGUMENTS
"""


# if you use both *args and **kwargs in the same function arguments, then *args needs to come first
# *args allows for an arbitrary number of arguments and places them in a tuple
def myfunc(*args):
    print(args)  # (40,60,20)
    return sum(args)


myfunc(40, 60, 20)  # 120


# **kargs allows an arbitrary number of keyword arguments and places them in a dictionary
def myfunc2(**kwargs):
    if "fruit" in kwargs:
        print(f"The fruit I like is: {kwargs['fruit']}")
    else:
        print("I don't like fruit")


myfunc2(fruit="apples")  # The fruit I like is apples


"""
DECORATORS
"""


# functions which modify the functionality of another function
def decorator_function(fn):
    print("this is printed first")
    fn()
    print("this is printed last")


@decorator_function
def func_to_be_passed_into_decorator():
    print("This function runs whenever called inside decorator_function")


print(func_to_be_passed_into_decorator())
# "this is printed first"
# "This function runs whenever called inside decorator_function"
# "this is printed last"


"""
USEFUL FUNCTIONS
"""

""" range function """
# range function is a generator function that allows you to quickly generate a list of integers
# 3 parameters are a start, stop, and a step size
list(
    range(0, 11)
)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], you need to cast it to a list to be able to use
list(range(0, 11, 2))  # [0, 2, 4, 6, 8, 10]

""" enumerate function """
# allows you to keep track of loop index easier
for i, letter in enumerate("abcde"):
    print(f"At index {i}, the letter is {letter}")
# format of output of enumerate('abcde") is [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')] and then we are tuple unpacking in for loop

""" zip function """
# allows you to combine two lists in tuple format
mylist1 = [1, 2, 3, 4, 5]
mylist2 = ["a", "b", "c", "d", "e"]
list(
    zip(mylist1, mylist2)
)  # output is [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

""" min, max functions """
min(mylist1)  # 1
max(mylist1)  # 5
