"""
if, elif, else statement
"""
if a > b:
    a = 2
elif a == b:
    a = 3
else:
    a = 10
# colon is used instead of () for if check
# indentation is used instead of {}

"""
for loop
"""
for item in object:
    print(item)
# for loop is an iterator (goes through items that are in a sequence or other iterable item)
# variable name can be anything you choose

# tuple unpacking
list2 = [(1, 2), (3, 4), (5, 6)]
for t1, t2 in list2:
    print(t1)  # 1,3,5

# dictionary unpacking
dict_var = {"k1": 1, "k2": 2, "k3": 3}
for k, v in dict_var:
    print(k, v)  # k1,1    k2, 2    k3,3


"""
while loop
"""
x = 0
while x < 10:
    print("x is: ", x)
    x += 1
else:
    print("all done")
