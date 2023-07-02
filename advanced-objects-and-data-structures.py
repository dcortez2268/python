"""
numbers
"""
""" hexadecimal"""
hex(246)  # "0xf6"
""" binary """
bin(1234)  #'0b10011010010'
""" exponentials """
pow(3, 4)  # 81, equivalent to 3^4
""" absolute value """
abs(-3.14)  # 3.14


"""
strings
"""
s = "hello world"
s.capitalize()  # 'Hello world'
s.upper()  #'HELLO WORLD'
s.lower()  #'hello world'
s.find("o")  # 4, returns index of first occurence


""" 
sets
"""
s = set()
""" add """
s.add(1)
s.add(2)
s.clear()  # {}
""" shallow copy """
s = {1, 2, 3}
sc = s.copy()
s.add(4)
sc  # {1, 2, 3}
""" difference """
s.difference(sc)  # {4}
""" difference update"""
s.difference_update(sc)  # 4
""" discard """
# removes an element from a set if it is a member
s.discard(4)  # {}
""" intersection """
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.intersection(s2)  # {1, 2}
{1, 2, 3}
""" intersection update"""
# intersection_update will update a set with the intersection of itself and another.
s1.intersection_update(s2)
s1  # {1, 2}
""" isdisjoint"""
# this method returns true if two sets have a null intersection
""" issubset """
# this method returns true if another set contains this set.
""" issuperset """
# this method returns true if this set contains another set.
""" symmetric difference """
# returns a new set with all elements that are in exactly one of the sets.
s1.symmetric_difference(s2)  # {4}
""" union """
# returns a set with all elements that are in either set.
s1.union(s2)  # {1, 2, 4}
""" update """
# updates a set with the union of itself and another set


"""
dictionaries
"""
""" dictionary comprehensions"""
# Just like List Comprehensions, Dictionary Data Types also support their own version of comprehension for quick creation. It is not as commonly used as List Comprehension
""" iteration over keys, values, and items"""
# remember they are a view so basically like a deep copy
d = {"k1": 1, "k2": 2}
for k in d.keys():
    print(k)  # k1 k2
for v in d.values():
    print(v)  # 1 2
for item in d.items():
    print(item)  # ('k1', 1) ('k2', 2)


""" 
lists
"""
list1 = [1, 2, 3]
""" append """
list1.append(4)  # list1 [1,2,3,4]
list1.append([4, 5])  # list1 [1,2,3,4,[4, 5]]
""" count """
list1.count(2)  # 1, counts the number of occurrences in list
""" extend """
list1.extend(10, 11)  # # list1 [1,2,3,4,[4, 5], 10, 11]
""" index """
list1.index(2)  # 1
list1.index(12)  # throws error if argument is not in list
""" insert """
# Place 'inserted' at the index 2
list1.insert(2, "inserted")
list1  # [1,2, 'inserted', 3,4,[4, 5], 10, 11]
""" pop """
# removes last element and returns by default, but you can specify index in argument to pop
""" remove """
# removes the first occurrence of a value.
""" reversed """
#  reverses a list. Note this occurs in place! Meaning it affects your list permanently.
""" sort """
# will sort your list in place:
# The sort() method takes an optional argument for reverse sorting. Note this is different than simply reversing the order of items.
list2.sort(reverse=True)
""" copying by value vs reference"""
x = [1, 2, 3]
y = x.append(4)
print(y)  # None, because the operation does not return a value, instead do this..
x = [1, 2, 3]
y = x.copy()  # copies by value
y.append(4)  # y == [1, 2, 3, 4]
x  # [1, 2, 3]

# using list(x) will return a copy by reference list
