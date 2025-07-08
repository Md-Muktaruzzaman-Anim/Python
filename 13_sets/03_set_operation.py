a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b) # Here a and b will combine all the unique values ​​together. a = {3, 23, 1}. b = {23, 4, 2, 55, 1}. union = {1, 2, 3, 4, 23, 55}. All unique elements will be there (duplicates removed)
print(c)

d = a.intersection(b) # Here only those values ​​will be common to both a and b. a = {3, 23, 1}. b = {23, 4, 2, 55, 1}. intersection = {1, 23}. Means those that are in both sets
print(d)

e = a.difference(b) # Here there will be only those elements that are in a but not in b. a = {3, 23, 1}. b = {23, 4, 2, 55, 1}. difference = {3}. Because 3 is only in a, not in b.
print(e)

'''
        a = {3, 23, 1}
        b = {23, 4, 2, 55, 1}

    ----------------------------
    union         = {1, 2, 3, 4, 23, 55}
    intersection  = {1, 23}
    difference    = {3}    (a - b)

    Bonus: b.difference(a)
# Output: {2, 4, 55}
'''