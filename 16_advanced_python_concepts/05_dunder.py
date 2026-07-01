class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"

    def __len__(self):
        return len(self.name)


e = Employee("Anim", 50000000)
print(len(e))
# print(e.name, e.salary)
# print(str(e))
# print(repr(e))



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2  # Calls __add__
print(v3)  # Vector(6, 8)
v4 = v3 - v1
print(v4)  # Vector(4, 5)
v5 = v1 * 5
print(v5)  # Vector(10, 15)