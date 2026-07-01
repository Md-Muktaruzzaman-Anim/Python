"""
Constructor is a special method that is automatically invoked when an object is created from a class.

Why is a constructor needed?
Through a constructor, we can directly set the necessary data when creating an object.
That is, a constructor initializes an object when it is created.

'''
Remember briefly:
Content                     explanation

__init__                    Python's constructor
When it runs                when creating an object
Work                        Initializes the properties of the object
self                        The object itself, for which the constructor is working
'''

Line-by-line explanation:
def __init__(self, salary, name, bond):
1. __init__ is a constructor (a special method in Python).
2. It runs automatically when an object is created.
3. In this method, we are taking 3 pieces of information:

salary
name
bond

Using these, we will set the data inside that object.

Remember in short:
Part                          name                                    Task

class Employee:               Class                                   A blueprint that will create an object.
def __init__(...)             constructor method                      Is invoked when the object is created.
self.salary = salary          Setting an instance variable            Stores information in the object.
"""
class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary # Create an instance attribute of name salary and assign it with salary. self.salary = Create a variable named salary inside the salary object and store the value.
        self.name = name # Create an instance attribute of name name and assign it with name. self.name = Store the name of the name object.
        self.bond = bond # Create an instance attribute of name bond and assign it with bond. self.bond = Store the bond/contract time of the bond object.

    def get_salary(self):
        return self.name, self.salary, self.bond
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")


e1 = Employee(34000, "John Doe", 4)
# print(e1.get_salary())
e1.get_info()

"""Explanation:
1. __init__ is the constructor — it will be invoked when you call Employee(...).
2. self.salary = salary — that is, the object you are creating is being set to its own salary.
3. In the get_salary() method, we are returning self.salary , that is, the salary of that particular object."""

class Person:
    def __init__(self, name, age):
        self.name = name  # Setting the name property of object.
        self.age = age    # Setting the age property of object.

    def introduce(self):
        print(f"I am {self.name}, and I am {self.age} years old.")

# Creating objects (this is where the constructor works).
p1 = Person("Anik", 25) # __init__ runs automatically when an object is created.
p2 = Person("Anim", 30) # __init__ runs automatically when an object is created.

p1.introduce()
p2.introduce()

# What's going on here?
# There is a constructor called __init__() inside the Person class.

# Whenever we write p1 = Person("Anik", 25), __init__() is automatically executed.

# self.name = name means that a property called name is created inside the object, whose value is "Anik".