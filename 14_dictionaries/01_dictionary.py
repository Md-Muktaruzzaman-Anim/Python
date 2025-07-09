'''
A dictionary is:

A collection of key-value pairs.
In a nutshell, a dictionary means — finding information by name.

Syntax of Dictionary:
dictionary_name = {
    key1: value1,
    key2: value2,
    key3: value3
}
'''
marks = {"Muktar": 34, "Anim": 40, "Anik": 90} # Here each item is a  key: value pair. The key is the student's name, and the value is the mark obtained by him.

# print(marks, type(marks))

# print(marks["Anik"]) # Here you are retrieving the value (marks) from the marks dictionary with the key named "Anik".
# marks["Muktar"] = 30 #Here you update the number of "Muktar" — earlier it was 34, now it will be 30. If the key exists in the Python dictionary, then when you give a new value, it replaces the old value.
marks["Anika"] = 85

print(marks)


'''
Task                                   code

Read value from dictionary             marks["Anik"]
Change value                           marks["Muktar"] = 30
Add new key                            marks["Anika"] = 85
Get type of dict                       type(marks)
'''