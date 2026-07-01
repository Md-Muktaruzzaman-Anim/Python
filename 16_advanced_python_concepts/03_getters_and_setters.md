🔍 In short:

Getter: To read the value of a private variable (attribute).

Setter: To change/set the value of a private variable.

📦 Let's take an example:
You create a Student class where you want to store its name and age. But you don't want anyone to directly enter the wrong value like student.age = -5. Then you can control it using setter.

🔍 code:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def first_name(self):  # Getter
        l = self.name.split(" ")
        return l[0]

    def set_first_name(self, first):  # Setter
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e = Employee("Tony Shark", 35000)

print(e.first_name())       # Output: "Tony"
e.set_first_name("Thor")    
print(e.name)               # Output: "Thor Shark"

What's going on here?
e = Employee("Tony Shark", 35000)
Here you've created an employee named Tony Shark.

e.first_name()
This is a Getter function — splitting the name and returning the first part (Tony).

e.set_first_name("Thor")
This is a Setter — splitting the name and updating it with the new first name:
"Tony Shark" → "Thor Shark"

🧠 Some important technical points (in Bengali):
split(" "):
You're splitting "Tony Shark" and getting a list → ["Tony", "Shark"]

new_name = f"{first} {l[1]}":
You're creating a new name where the first part is "Thor" and the second part is "Shark" from the old name.

You've created the getter/setter yourself (manual), but you could have done it the Pythonic way (decorator @property) if you wanted.
Bonus: What if you did the same thing with @property?

🔍🔍🔍
What is the @property decorator and why do we use it?
First, we need to know what the @property decorator is. When we create a class in Python, we call the variables inside the class attributes. For example, in your Employee class, name and salary are attributes.

Many times we don't want these attributes to be changed or accessed directly. We want to have some special rules for accessing and modifying them. That's where the @property decorator comes in handy.

Simply put:

1. The @property decorator creates a method in such a way that it can be used like an attribute. This means that you can access it like an attribute without calling the method directly using the . (dot) operator.

2. This allows you to add special logic while accessing the attribute. For example, performing some calculations before getting the value of an attribute or validating an attribute before setting its value.

We can call this a Pythonic way of creating "getter" and "setter" methods.

Detailed explanation of  code:

Let's analyze the code line by line:

Employee class:

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

1.Here we have created a class named Employee.

2. The __init__ method is the constructor. Whenever a new object of the Employee class is created, this method is automatically executed.

3. It takes two parameters named name and salary and stores them in the object as self.name and self.salary attributes.

@property as first_name (getter):

@property
    def first_name(self):
        """
        This is the 'getter' method. 
        It's accessed like an attribute (e.g., e.first_name).
        """
        l = self.name.split(" ")
        return l[0]

1. Here the @property decorator is used on the method first_name . This means that you can access it like an attribute like e.first_name , without having to call the method like e.first_name() .

2. This method creates a list by splitting the value of the self.name attribute with spaces (" ") (l = self.name.split(" ")). For example, "Tony Shark" becomes ['Tony', 'Shark'].

3. It then returns the first element of the list (l[0]), which is the first name. This is the getter method, which does the work of "getting" the value of the attribute.

@first_name.setter as first_name (setter):

@first_name.setter
    def first_name(self, first):
        """
        This is the 'setter' method.
        It's used when assigning a value (e.g., e.first_name = "Thor").
        The method name MUST match the property name.
        """
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

1. Notice that this method uses @first_name.setter . This means that this is the setter method for the first_name property.

2. This method is automatically called when you assign a value to the first_name property, such as e.first_name = "Thor".

3. This method takes a parameter (first) that contains the newly assigned value.

4. Internally, it extracts the last name from the current self.name (l[1]).

5. It then adds the new first name (first) and the old last name (l[1]) to create a new full name (new_name).

6. Finally, it updates the self.name attribute with this new_name.

Code Execution:

# Create an instance of the Employee
e = Employee("Tony Shark", 35000)

1. Here an object e of the Employee class is created, named "Tony Shark" and with a salary of 35000.

# 1. Access the property like an attribute (no parentheses)
print(e.first_name)

1. When print(e.first_name) is written, the first_name attribute is being accessed.

2. In this case, the getter method first_name() created by the @property decorator is called.

3. This extracts "Tony" from "Tony Shark" and prints it.

4. Output: Tony

# 2. Use the setter by assigning a new value to the property
e.first_name = "Thor"

1. Here, e.first_name = "Thor" is assigning a new value ("Thor") to the first_name property.

2. In this case, the setter method first_name(self, first) created by the @first_name.setter decorator is called, where the value of first is "Thor".

3. The setter method takes the "Shark" part from self.name ("Tony Shark").

4. It then combines "Thor" and "Shark" to change self.name to "Thor Shark".

# 3. Print the full name to see the change
print(e.name)

1. Finally, print(e.name) prints the current value of the name attribute of the e object.

2. Since the setter method changed self.name to "Thor Shark", that is what will be printed.

3. Output: Thor Shark

🚀 Benefits of using @property
Data Encapsulation: It helps to control the internal data of the class. You can decide how the data will be accessed or modified.

Code Readability: Since it can be accessed like an attribute, the code is easy to read and feels like the data is being accessed directly, not a method call.

Validation Logic: Inside the setter method, you can add various validation rules before setting the data, for example: Can salary be negative?

Backward Compatibility: If your code already uses attributes, and you later want to control access to those attributes, you can add methods using @property, but users won't have to change their code.