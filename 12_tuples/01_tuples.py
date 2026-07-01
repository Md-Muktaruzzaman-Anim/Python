'''
A tuple is a Python data structure that is similar to a list —
but once created, it cannot be modified.

Tuple properties:

Feature                Description
Immutable              Once created, the value cannot be changed
Ordered                Elements have a specific/fixed order (index)
Iterable               Can be iterated through a loop
Faster than list       Slightly higher performance than list

Note: If the tuple has only one element, then a comma (,) must be given — otherwise it will not be a tuple, but will be treated as a number.
'''

a = (3, 2, 22, 34)

print(a)
print(a[2])

b = (1, )