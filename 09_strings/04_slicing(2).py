# name = "Python"
# print(name[0:2]) # → 'Py' (index 0 and 1)

# print(name[1:4]) # → 'yth' (index 1, 2, 3)

# print(name[2:] ) # → 'thon' (from index 2 to end)

# print(name[:3] ) # → 'Pyt' (from start to index 2)

# print(name[:-1]) # → 'Pytho' (till before last character)

# print(name[-3:]) # → 'hon' (last 3 characters)

"""e.g.

string[start : stop : step]

start: where to start (take the index)

stop: where to stop (take up to this index)

step: how many steps to take (i.e. how many characters to skip)

step = 1 → nothing is skipped

step = 2 → 1 character is skipped

step = 3 → 2 characters are skipped

The larger the step, the more characters are skipped"""

name = "0123456789"

# print(name[0:10:n]) # skip n-1 character
print(name[0:10:1]) # skip 0 character
print(name[0:10:2]) # skip 1 character
print(name[0:10:3]) # skip 3-1 ie 2 character