"""
dynamic typing, type checking
"""
dynamic_var = 2  # vars are lowercase, with _ in between words
dynamic_var = ["hi", "hello"]

type_check = type(integer_var)  # int
type_check = type(floating_point_var)  # float
type("hi")  # str
# other types: list, tuple, dict, set, bool

"""
floating point, integer, mod operator, ** operator
"""
floating_point_var = 3.0
floating_point_var1 = 3.5
integer_var = 3
integer_var1 = -3
mod_var = 10 % 4  # 2
exponent_var = 2**3  # 8
division_var = 3 / 2  # 1.5
division_var1 = 3 // 2  # 1, // reprents floor division


"""
STRINGS
"""
# are immutable, you can change variable assignment, and can concatenate, but cannot change an index's value
# you can use single or double quotes

len("12 345")  # 6, returns length of a string, including spaces
second_character = "hello"[1]  # e, strings can be indexed
sliced_string = "hello"[1:]  # "ello"
sliced_string = "hello"[:3]  # "hel"
sliced_string = "hello"[:3]  # "hel"
sliced_string = "hello"[:-1]  # "hell"
concatenated_string = "he" + "llo"  # hello

# string interpolation
# 3 different implementations, depending on which version you use
# f strings are the recommended implementation:
name = "dominick"
print(f"{name} goes here")

print("this string implements the {} method".format(".format()"))  # format method
print("this string implements the {f} method".format(f=".format()"))  # format method
# last method is using the modulo operator, but avoid using if possible


"""
LISTS
"""
# data structure that contain elements stored in an array
# lists can be indexed, nested, concatenated, store different data types, and are mutable
list_var = [1, 2, "some string"]

list_var.
""" LIST COMPREHENSIONS """
# allow us to build out lists using a different notation
# basically a one line for loop built inside of brackets
new_list = [expression for item in iterable if condition]
[x for x in "word"]  # ['w', 'o', 'r', 'd']
[x**2 for x in range(0, 11)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

""" allow if statements, nested list comprehensions """
[x for x in range(11) if x % 2 == 0]  # [0, 2, 4, 6, 8, 10]
[ x**2 for x in [x**2 for x in range(11)]]  # [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]


"""
DICTIONARIES
"""
# data structure that consists of key-value pairs where keys and value can be almost any python object
# unordered, hash table
# dictionaries can be nested
dictionary_var = {"key1": "value1", 45: 2, "key3": [3234, 3, "hi"]}
dictionary_var["key1"]  # "value1"
dictionary_var["key4"] = "value4"  # can add values via assignment
.items(), .values(), .keys() # provide a view or reference of the dictionary's corresponding elements(depending on method) in an array, elements dynamically change if dictionary changes because they provide reference


"""
TUPLES
"""
# immutable data structure that contains elements stored in parenthesis
# like lists, but are immutable, and therefore not as flexible or useful
# tuples size cannot grow once initialized
tuple_var = (1, 2, "hi")


"""
SETS, BOOLEANS
"""
# sets are unordered collection of unique elements
# whenever you add an item twice, it does not throw an error but it won't add the element twice
set_var = set()
set_var.add(1)
print(set_var)  # {1}

# booleans are variables with True or False value
# true represents 1, and false 0
true_var = True
false_var = False
null_var = None  # implemented when we don't want to assign a variable yet, like null in other languages


"""
OPERATORS
"""
true_var == true_var  # true, true if operands are equal
1 < 2 < 3  ## true, reads as "1 is less than 2" AND "2 is less than 3"

""" IN OPERATOR """
# implemented to check if object is in list
'x' in ['x','y','z'] # true
""" NOT IN OPERATOR """
'a' not in ['x','y','z'] # true




