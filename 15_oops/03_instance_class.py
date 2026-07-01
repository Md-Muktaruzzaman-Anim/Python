'''
Understand how the code is works:

Create a variable named salary inside this object (Employee) and put the value of salary sent from outside in it.

So let's break down this line self.salary = salary:
Part                         means

self.salary                  The salary property inside the object (a separate variable).

=                            Setting the value.

salary                        The parameter that comes in the constructor, meaning the salary sent from outside.

e1 = Employee(34000, "John", 3, "NASA")
If you run this line:
salary parameter will be 34000.
name parameter will be "John".
bond parameter will be 3.
company parameter will be "NASA".

def __init__(self, salary, name, bond, company):
    self.salary = salary   # এখানে self.salary = 34000
    self.name = name       # self.name = "John"
    self.bond = bond       # self.bond = 3
    self.company = company # self.company = "NASA"

    This self.salary, self.name, etc. are the own data inside this object, which you can use later in any method.


Suppose you fill out a student form.
def __init__(self, name, age):
    self.name = name
    self.age = age

This means:
"Put the value name in the name field of this student object, and the value age in the age field."
If self.salary = salary were not written:
Then no data named salary would be stored inside the object — meaning you wouldn't be able to see that salary from get_salary() or get_info().

Easy to remember trick:
1. self.salary → The place inside the object where we will put salary.
2. salary → The data passed to the constructor (e.g.: 34000).
3. self.salary = salary → means “Keep 34000 as salary for this object.”.

🔍 Bonus Tip: What does self mean?
self means the object itself, for which the work is being done.

For example:
    e1 = Employee(34000, "John", 3, "NASA")

Here self means e1.
And if you make e2 = Employee(...), then self means e2.
'''


# class Employee:
#     company = "Linux" # This is class attribute.

#     def __init__(self, salary, name, bond, company):
#         self.salary = salary # Create an instance attribute of name salary and assign it with salary. self.salary = Create a variable named salary inside the salary object and store the value
#         self.name = name # Create an instance attribute of name name and assign it with name. self.name = Store the name of the name object.
#         self.bond = bond # Create an instance attribute of name bond and assign it with bond. self.bond = Store the bond/contract time of the bond object.
#         self.company = company

#     def get_salary(self):
#         return self.name, self.salary, self.bond
    
#     def get_info(self):
#         print(f"The name of the employee is {self.name}. Salary is {self.salary}. The bond is for {self.bond} years.")


# e1 = Employee(34000, "John", 3, "NASA")

# e1.get_info()
# print(e1.get_salary())

# print(e1.company) # Will always print instance attribute whenever present and if it is not present then this will print class attribute. Output: NASA, because NASA is since instance attribute.
# print(Employee.company) # Employee is the name of the class. This will always print the class attribute.


# Object introspection
# print(dir(e1))




'''
Definition:

Name                                 What?                                        Where is it located?
                
Instance Attribute                   Each object has its own data                 Created with self.variable.
Class Attribute                      Same data for all objects                    Lives directly inside the class (outside the constructor).


🧠 Memorization trick:
🧍‍♂️ Instance attribute → Different value for each individual (object)
🏢 Class attribute → Same value for the entire class


# Remember in brief:

# Difference               Instance Attribute                 Class Attribute

# How to create            self.name = value                  name = value (directly inside the class)
# Where does it affect     Only on that object                all objects
# used on                  If you need different data         If you need one data for everyone

🧠 Remember with examples:
Your own name and age → instance attribute
Your nationality (American) → class attribute
'''


class Employee:
    company = "Google"   # ← Class Attribute

    def __init__(self, name, salary):
        self.name = name      # ← Instance Attribute
        self.salary = salary  # ← Instance Attribute


e1 = Employee("Anik", 30000)
e2 = Employee("Muktar", 50000)

print(e1.name)      # Output: Anik   → Separate instance attribute
print(e2.name)      # Output: Muktar   → Separate instance attribute

print(e1.company)   # Output: Google  → Same class attribute
print(e2.company)   # Output: Google  → Same class attribute

e1.company = "Amazon"  # Now I have created a separate company just for e1.

print(e1.company)  # Output: Amazon    (e1's own)
print(e2.company)  # Output: Microsoft (Previous class attribute for the rest)