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
# returns the difference of two or more sets as a new set
new_set = s.difference(sc)  # new_set = {4}
""" difference update"""
# removes all elements of another set from this set
s.difference_update(sc)  # s = {4}
new_set = s - sc # same as s.difference_update(sc), new_set = {4}

""" discard """
# removes an element from a set if it is a member, DOES NOT raise a KeyError if element is not a member of a set
s.discard(4)  # {}

""" remove """
# removes an element from a set if it is a member, raises a KeyError exception if element is not a member of a set
s.remove(4)  # KeyError

""" intersection """
# returns the intersection of a set and the set of elements in an iterable
s1 = {1, 2, 3}
s2 = {1, 2, 4}
s1.intersection(s2)  # {1, 2}
s1 & s2 # same as s1.intersection(s2), returns set of {1,2}
{1, 2}
""" intersection_update"""
# intersection_update will update a set with the intersection of itself and another.
s1.intersection_update(s2)
s1  # {1, 2}
s1 &= s2 # {1, 2}, same as intersection_update

""" isdisjoint"""
# this method returns true if two sets have a null intersection
""" issubset """
# this method returns true if another set contains this set.
""" issuperset """
# this method returns true if this set contains another set. can also use the > operator

""" symmetric difference """
# returns a new set with all elements that are in exactly one of the sets.
new_set = s1.symmetric_difference(s2)  # new_set = {4}
new_set = s1 ^ s2  # new_set = {4}, ^ operator is the same as .symmetric_difference()
""" symmetric_difference_update """
# updates a set with all elements that are in exactly one of the sets.
s1.symmetric_difference_update(s2)  # s1 = { 3, 4}
s1 ^= s2  # s1 = { 3, 4}, ^= operator is the same as .symmetric_difference_update()

""" union """
# returns a set with all elements that are in either set.
s1.union(s2)  # {1, 2, 4}
s1 | s2 # equivalent to s1.union(s2) {1, 2, 4}

""" update """
# updates a set with by adding elements from another set
# update only works for iterable objects
s1.update( s2 ) # s1 = {1,2,3,4}
s1 |= s2 # same as s1.update( s2 )


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
list1.extend([10, 11])  # # list1 [1,2,3,4,[4, 5], 10, 11]
""" index """
list1.index(2)  # 1
list1.index(12)  # throws error if argument is not in list
""" insert """
# Place 'inserted' at the index 2
list1.insert(2, "inserted")
list1  # [1,2, 'inserted', 3,4,[4, 5], 10, 11]
""" pop """
# removes last element and returns by default, but you can intecify index in argument to pop
""" remove """
# removes the first occurrence of a value.
""" reversed """
#  reverses a list. Note this occurs in place! Meaning it affects your list permanently.
""" sort """
# will sort your list in place:
# The sort() method takes an optional argument for reverse sorting. Note this is different than simply reversing the order of items.
list2.sort(reverse=True)
""" shallow copy """
x = [1, 2, 3]
y = x.append(4)
print(y)  # None, because the operation does not return a value, don't do this..
y = x # would copy x's reference, don't do this
x = [1, 2, 3]
y = x.copy()  # shallow copy
y.append(4)  # y == [1, 2, 3, 4]
x  # [1, 2, 3]
# using list(x) will return a shallow copy as well
""" join()"""
'delimiter'.join(list_of_strings) # the delimiter is a string that will be inserted between each string in list_of_strings
""" split()"""
# splits string into list of substrings based on a specified delimiter, if no demiliter defaults to space
# returns list
str.split(delimiter, optional maxsplit)


""" 
booleans
"""
# to compare an iterable of booleans you can use any and all
booleans = [True, False, True, True]
isTrue = any(booleans) # returns True if there is one True in iterable
isFalse = all(booleans) # returns True if there is all True values in iterable
