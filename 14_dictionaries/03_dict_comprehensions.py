'''
Dictionary comprehension is a shortcut technique through which a new dictionary can be created very easily and with less code.

It works like a for loop, but in one line.

🔹 General structure (Syntax):
new_dict = {key_expr: value_expr for item in iterable}

key_expr means "key expression" — that is, the value that will be used as a key in dictionary comprehension is called key_expr.

🔸 Here, key_expr → key will be
🔸 value_expr → value of that key will be
🔸 iterable → from which the value will come (list, range, dict, etc.)
'''

table_of_10 = {i: 10*i for i in range(1,11)}
print(table_of_10)