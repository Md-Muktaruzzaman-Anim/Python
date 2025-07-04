# String formatting

'''String formatting is a powerful feature in Python that allows you to insert variables and expressions into strings in a structured way. Python provides multiple ways to format strings, including the older format() method and the modern f-strings .'''

# template = "Dear {}, You are awesome. Take this {} bag."
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c1 = 300

# s1 = template.format(a,a1)  # use old version of Python
# print(s1)

print(f"{a} you are awesome and take this {a1}$ bag.")
print(f"{b} you are awesome and take this {b1}$ bag.")
print(f"{c} you are awesome and take this {c1}$ bag.")

# ord() and chr() - Character Encoding
#     Ascii value

# print(ord('A')) # Output: 65
# print(chr(65)) # Output: 'A'