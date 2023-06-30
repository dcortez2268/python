"""
generators
"""


# Generators allow us to generate as we go along, instead of holding everything in memory.
# Generator functions allow us to write a function that can send back a value and then later resume to pick up where it left off.
# Generators are best for calculating large sets of results (particularly in calculations that involve loops themselves) in cases where we don’t want to allocate the memory for all of the results at the same time.
def gencubes(n):
    for num in range(n):
        yield num**3  # yield keyword causes a function to become a generator


for x in gencubes(10):
    print(x)
# 0,
# 1,
# 8 , ...

# The next() function allows us to access the next element in a sequence.
x = gencubes(10)
next(x)  # 0
next(x)  # 1
next(x)  # 8

# The iter() function allows us to directly iterate over an iterable object as we could with a generator function
str_iter = iter("hello")
next(str_iter)  # "h"
next(str_iter)  # "e"
next(str_iter)  # "l"
