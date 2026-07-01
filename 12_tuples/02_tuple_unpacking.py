# Unpacking means:
# Dividing multiple values ​​in a data structure (like a tuple, list, set) into multiple variables.
# Simply put:
# Think of a box (like a tuple), which has many things inside.
# Unpacking means:
# You open the box and put each thing in a separate place.
'''
⁜⁜ It is crucial to understand this.

a, b, c = tup
Why not write: tup = a, b, c instead
Actually, both lines are valid Python, but they do very different things.
1. a, b, c = tup → Tuple Unpacking
This means:
Take values from tup and assign them to variables a, b, and c.
2. tup = a, b, c → Tuple Packing
This is the opposite — it means:
Take variables a, b, and c, and pack them into a tuple named tup.
# Summary:
Code	            What it does	                Direction            
a, b, c = tup	Unpacks values into variables	Tuple → Variables
tup = a, b, c	Packs variables into a tuple	Variables → Tuple

⁂⁂ Unpacking: Extracting values ​​from a tuple and storing them in separate variables.

⁂⁂ Packing: Creating a tuple from separate variables.
'''

tup = (3, 2, 1)

a, b, c = tup # This will simply assign a with 3, b with 2, c with 1

print(a, b, c)