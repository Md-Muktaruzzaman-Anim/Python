class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method (default)
    def print_info(self):
            info = f"The name is {self.name} and the salary is {self.salary}"
            print(info)

     #Static method
    @staticmethod  # Static methods does not use the instance attribute.
    def sum(a, b):
         return a + b
    
    # Class methods
    @classmethod
    def print_company(cls):
         print(cls.company)

    @classmethod
    def change_company(cls, new_company):
         cls.company = new_company

e1 = Employee("Jack", 20000)
e2 = Employee("Jill", 30000)

# print(Employee.company)
# print(Employee.name) # This will throw an error.

# e1.print_info()
# e2.print_info()

# print(e2.sum(23,7))
print(Employee.company)
e1.change_company("Nvidia")
print(Employee.company)