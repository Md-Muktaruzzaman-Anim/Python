marks = {"Muktar": 34, "Anim": 40, "Anik": 90}

print(marks.keys())
print(marks.values())

# marks.pop("Anim")
# marks.clear()

# If this method does not have a key, it returns None.
# But writing marks["Anika"] will throw a KeyError and it shows none
# print(marks.get("Anik"))     # Output: 90
# print(marks.get("Anika"))    # Output: None (Error দেয় না!)

# update() → Add one or more new items to dict or update old ones
# marks.update({"Anika": 85, "Muktar": 50})

# popitem() → removes the last key-value pair
# last = marks.popitem()
# print(last)   # Example: ('Anik', 90)

print(marks)


"""
Method                      Task

get(key)                    retrieves value safely
keys()                      returns all keys
values()                    returns all values
items()                     returns all key-value pairs
update()                    returns new or updated key-values
pop(key)                    removes specified key-value
popitem()                   removes last key-value
clear()                     empties dict
in                          checks if key exists
"""