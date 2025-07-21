class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        """
        This is the 'getter' method. 
        It's accessed like an attribute (e.g., e.first_name).
        """
        l = self.name.split(" ")
        return l[0]
    
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

# Create an instance of the Employee
e = Employee("Tony Shark", 35000)

# 1. Access the property like an attribute (no parentheses)
print(e.first_name)

# 2. Use the setter by assigning a new value to the property
e.first_name = "Thor"

# 3. Print the full name to see the change
print(e.name)