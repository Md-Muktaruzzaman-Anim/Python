name = "Anim"

# Index:     0   1   2   3
# Letters:   A   n   i   m
# Negative: -4  -3  -2  -1

# string[start:stop] # Here it starts from start and goes to stop-1. The stop index is omitted.

print(name[0:4]) # Here it starts from 0 and goes to 2-1. The stop index is omitted. index 0 and 1. [Output: An]
print(name[0:4]) # Here it starts from 0 and goes to 4-1. The stop index is omitted. index 0, 1, 2 and 3. [Output: Anim]

print(name[0:-1]) # Index will be taken starting from 0 and ending before the -1. [Output: Ani]

print(name[0:-1]) # Index will be taken starting from 0 and ending before the -1.


# e.g.

''' Code               Output Explanation

  name[0:2]           "An" index 0 and 1
  name[0:-1]          "Ani" index 0, 1 and 2
  name[2:3]           "i" only index 2 '''