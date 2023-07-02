"""
collections module
"""
# implements specialized container data types in addition to python's built in container types (list, dict, set, and tuple)


""" Counter """
from collections import Counter

lst = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]
Counter(lst)  # {1: 6, 2: 6, 3: 4, 12: 1, 21: 1, 32: 1, 223: 1}


""" defaultdict """
# dictionary-like object which provides all methods provided by a dictionary but takes a first argument (default_value_or_object) as a default data type for the dictionary.
# A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default_value_or_object argument
from collections import defaultdict

d = defaultdict(object)  # d is empty defaultdict
d["one"]  # <object at 0x216de27bcf0>


""" namedtuple """
# assigns names, as well as the numerical index, to each member.
# You can basically think of namedtuples as a very quick way of creating a new object/class type with some attribute fields.
from collections import namedtuple

Dog = namedtuple("Dog", ["age", "breed", "name"])
sam = Dog(age=2, breed="Lab", name="Sammy")
sam.age  # 2
sam.breed  # "Lab"


"""
datetime module
"""
# help deal with times and dates in your code.
# Time values are represented with the time class.
# Date values are represented with the date class.
import datetime

t = datetime.time(4, 20, 1)
d = datetime.date.today()


"""
math and random
"""
""" random module """
import random
from random import randint
random.seed(
    101
)  # setting a seed allows us to ensure random numbers will show up in a series, 101 is a arbitrary number, anything can be set here
randint(0, 100)  # Return random integer in range [0, 100], including both end points.


""" math module"""
import math

value = 4.35
math.floor(value)  # 4
math.ceil(value)  # 5
round(value)  # 4
math.pi  # 3.14
math.e  # 2.718281828459045


""" pdb module"""
# python debugger module
import pdb


""" regular expressions module"""
import re

search_str = " This is string to search"
pattern = r"string"  # an r string tells python this is a regular expression string so that \ in the pattern string are not meant to be escape slashes
pattern in search_str  # True
re.search(pattern, search_str)  # <_sre.SRE_Match object; span=(13, 18), match='phone'>
re.search("Jose", search_str)  # None
# | is the or operator
# . is the wildcard operator, a . is needed for each character


""" timing code modules"""
# used if code is > 0.1 s
import time

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

# used if code is < 0.1s
# runs code several times and then reports average length of time it took
import timeit


"""
zipping files
"""
""" zipfile module"""
import zipfile
""" shutil module"""
# archives everything at once
import shutil


"""
WEB SCRAPING
"""
''' commands to run to install modules'''
pip install requests
pip install lxml
pip install bs4

