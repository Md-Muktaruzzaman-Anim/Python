1. Instance Method 🧑‍💻
First we will talk about instance method. It is the most common method that we usually use. Instance method is associated with an instance (or object) of a class. It can access and modify the data of the instance (using self parameter).

Example through story:

Let's say, we have a 'Student' 👨‍🎓 class. Each student has his/her own name, roll number and GPA. Now, we want to create a method to check 📝 the result of a student's own exam. This method will use the GPA data of that particular student.

2. Class Method 🏫
A class method is associated with the class itself, not with any specific instance. It can access and modify the class's data (called class variables). The first parameter of a class method is usually cls, which refers to the class. It is defined using the @classmethod decorator.

Example through a story:

In our 'student' 👨‍🎓 class, suppose the university authorities want to tell everyone how many students have been admitted this year 🧑‍🎓➕🧑‍🎓. This information is not related to a specific student, but to the entire class. Class methods are used to handle such information.

3. Static Method 🛠️
A static method cannot access the data of an instance or class  it works like a normal function, which is related to a class but does not depend on the data of the class or instance itself. It is only placed inside a class to organize the code. It is defined using the @staticmethod decorator.

Example through the story:

Let's go back to our 'Student' 👨‍🎓 class. Suppose, the university authorities want to have a simple calculator ➕➖✖️➗ functionality, which can convert any student's GPA to grade. To do this, no specific student information (such as name, role) is required, just the GPA number is enough. This is a simple utility function that is associated with the class but does not access the class's own data or instance data.


🧩🧩🧩

### What are Instance, Static, and Class Methods?

In Python, a class can have different types of methods. These methods are defined based on how they interact with the class or its objects. The three main types of methods are:

1. Instance Method: A method that works with a specific object (instance) of a class. It typically uses the self parameter to access the object's data (attributes).
2. Static Method: A method that is not directly related to the class or object's attributes. It behaves like a regular function within the class's namespace and is defined using the @staticmethod decorator.
3. Class Method: A method that works with the class itself and accesses classlevel data (class attributes). It uses the cls parameter and is defined using the @classmethod decorator.

Let’s now explain these three types of methods in detail using the provided code.



### Code Analysis

class Employee:
    company = "HP"  # Class attribute (static variable)

    def __init__(self, name, salary):
        self.name = name  # Instance attribute
        self.salary = salary  # Instance attribute

    # Instance method
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static method
    @staticmethod
    def sum(a, b):
        return a + b
    
    # Class method
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jack", 20000)  # First object
e2 = Employee("Jill", 30000)  # Second object

print(Employee.company)  # Output: HP
e1.change_company("Nvidia")  # Change class attribute
print(Employee.company)  # Output: Nvidia




### 1. Instance Method

Explanation:
An instance method is a method that operates on a specific object (instance) of a class. It typically takes self as its first parameter, which refers to the instance calling the method. This method can access the instance attributes (e.g., name, salary) of the object.

Code Example:

def print_info(self):
    info = f"The name is {self.name} and the salary is {self.salary}"
    print(info)


 Here, print_info is an instance method. It uses the self parameter, which refers to the object (e.g., e1 or e2).
 self.name and self.salary are instance attributes, unique to each object.
 When we call e1.print_info(), it uses the name and salary of the e1 object. For example:
 
  e1.print_info()  # Output: The name is Jack and the salary is 20000
  e2.print_info()  # Output: The name is Jill and the salary is 30000
  

When to Use?
 When you need to access or manipulate the specific data (instance attributes) of an object.
 Example: Printing an employee's name and salary.

Explanation in English:
An instance method is a function that works with a specific object of a class. It can access the object’s data (e.g., name, salary) and is used when we want different results for each object.



### 2. Static Method

Explanation:
A static method is a method that does not depend on the class or object’s attributes. It behaves like a regular function but resides within the class’s namespace. It is defined using the @staticmethod decorator and does not take self or cls as a parameter.

Code Example:

@staticmethod
def sum(a, b):
    return a + b


 Here, sum is a static method. It does not use any class or object data (e.g., name, salary, or company).
 It simply adds two numbers (a and b) and returns the result.
 It can be called using either the class or an object. For example:
  python
  print(e2.sum(23, 7))  # Output: 30
  print(Employee.sum(23, 7))  # Output: 30
  

When to Use?
 When a method does not need to access class or object data and performs a general task related to the class.
 Example: A utility function like adding numbers that is logically related to the class but does not depend on its attributes.

Explanation in English:
A static method is a function that resides within a class but does not use class or object data. It acts like an independent function and can be called using the class or an object. It is used for general tasks related to the class.



### 3. Class Method

Explanation:
A class method is a method that works with the class itself and accesses classlevel data (class attributes). It is defined using the @classmethod decorator and takes cls as its first parameter, which refers to the class.

Code Example:

@classmethod
def print_company(cls):
    print(cls.company)

@classmethod
def change_company(cls, new_company):
    cls.company = new_company


 Here, print_company and change_company are class methods.
 print_company prints the company class attribute.
 change_company modifies the company class attribute.
 Example:
  python
  print(Employee.company)  # Output: HP
  e1.change_company("Nvidia")  # Change class attribute
  print(Employee.company)  # Output: Nvidia
  
 Notice that calling e1.change_company("Nvidia") changes the company attribute for the entire class, as it is a shared class attribute.

When to Use?
 When you need to access or modify classlevel data (class attributes).
 Example: Changing or printing a shared class attribute like the company name.

Explanation in English:
A class method is a function that works with the class itself and accesses classlevel data (e.g., company). It uses the cls parameter to interact with class attributes. It is used when we want to work with data shared across all objects of the class.



### Key Differences (Summary)

 Type                               First Parameter                    Function                                                                              Example                     

 Instance Method                    self                               Works with objectspecific data (instance attributes).                                 e1.print_info()              
 Static Method                      None                               Independent of class/object data, behaves like a regular function.                    Employee.sum(23, 7)          
 Class Method                       cls                                Works with classlevel data (class attributes).                                        e1.change_company("Nvidia")  



### Explanation of Code Output

1. First Print (HP):
    Employee.company accesses the class attribute, which is a shared variable for the class.
2. Company Change (Nvidia):
    e1.change_company("Nvidia") uses the class method to modify the company class attribute, which is shared across all objects.