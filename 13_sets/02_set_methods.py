# In Python, a set is:

# Unordered, hash-based collection
# This means that Python uses a hash table to store the values ​​of the set in memory. Therefore, their order is always random.

s = {34, 23, 1, 3, 22}

print(s)

# s.add(32)
# s.add(420)
# s.remove(1)

'''
Method             What if there is no item?.
remove(x)          Will throw Error (KeyError).
discard(x)         Will do nothing silently.
'''

# s.remove(1234) # If you try to remove something that is not in the set, then remove() will crash horribly, because 1234 is not in the set. If you are sure that the item is in the set, use remove().

# s.discard(1234) # discard() will silently check: Is the item there? No? Then do nothing.  If you are not sure, or don't want an error, use discard().
# print(s)
'''
Method            Action

pop()             removes 1 element and returns
remove(x)         removes the specified item (Error if none)
discard(x)        removes the specified item (silently if none)
'''
x = s.pop()
print("Removed:", x)
print("Now set:", s)
