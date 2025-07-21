Magic methods, also called dunder (double underscore) methods, are special
methods in Python that have double underscores at the beginning and end of their
names (e.g., __init__ , __str__ , __add__ ). These methods allow you to define
how your objects interact with built-in Python operators, functions, and language
constructs. They provide a way to implement operator overloading and customize
the behavior of your classes in a Pythonic way.

They are used to:

Customize object creation and initialization ( __init__ , __new__ ).
Enable operator overloading (e.g., +, -, *, ==, <, > )

Otherwise:

Magic or dunder (double underscore) methods are special methods in Python that customize the behavior of a class, such as initialization, arithmetic operations, or string representation. They are defined with a double underscore, such as __init__, __str__.

Purpose:

1. Custom behavior for built-in operations (such as +, len(), string conversion).
2. Makes the class look Pythonic and intuitive.
3. Common mistakes: Incorrect method signature, missing return value, or not calling super.

⁂⁂ Explanation (init, str, repr):

1. __init__(self, name, salary):
Constructor method. Called when creating an object. It initializes the name and salary.
Example: e = Employee("Anim", 50000000) sets self.name = "Anim", self.salary = 50000000.

2. __str__(self):
Returns the string representation of the object, used when calling print() or str(). Easy for the user to understand.
Example: print(str(e)) returns "The name is Anim and the salary is 50000000".

3. __repr__(self):
Returns the formal string representation of the object, useful for developers. Called repr() or in an interactive shell.
Example: print(repr(e)) returns "name: Anim\nsalary: 50000000".

Output Explanation:

e = Employee("Anim", 50000000)
print(e.name, e.salary)  # Output: Anim 50000000
print(str(e))            # Output: The name is Anim and the salary is 50000000
print(repr(e))           # Output:  name: Anim
                         #          salary: 5000000

Differences:

1. __str__: User-friendly string, usually short.
2. __repr__: Developer-friendly, verbose, often useful for object reconstruction.
3. Pitfall: __str__ or __repr__ will cause an error if they do not return a string.


🎯 Code: 
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

🎯🎯 Explanation:

 1. __init__(self, x, y): The Constructor 🛠️

This is the constructor method. It's automatically called whenever you create a new instance of the Vector class.

1. self: This refers to the instance of the Vector class being created. It's a convention in Python methods to have self as the first parameter, allowing you to access and modify the instance's attributes.
2. x, y: These are the initial values passed when creating a Vector object (e.g., Vector(2, 3)).
3. self.x = x and self.y = y: These lines initialize the instance variables x and y for the Vector object. So, when you write v1 = Vector(2, 3), v1 will have its x attribute set to 2 and its y attribute set to 3.

How it works: When you execute v1 = Vector(2, 3), Python internally does something like Vector.__init__(v1, 2, 3). The __init__ method then sets up the v1 object with the provided x and y values.

 2. __add__(self, other): Operator Overloading for Addition ➕

This Dunder method enables the use of the + operator for Vector objects. It allows you to overload the addition operator, meaning you can define its behavior for your custom class.

1. self: This is the Vector object on the left side of the + operator (e.g., v1 in v1 + v2).
2. other: This is the Vector object on the right side of the + operator (e.g., v2 in v1 + v2).
3. return Vector(self.x + other.x, self.y + other.y): This line defines what happens when you add two Vector objects. It creates a new Vector object where the x components are added together and the y components are added together.

How it works: When you execute v3 = v1 + v2, Python recognizes the + operator applied to Vector objects. It then calls v1.__add__(v2). The __add__ method adds the x and y components of v1 and v2 respectively, returning a new Vector object (e.g., Vector(2+4, 3+5) = Vector(6, 8)), which is then assigned to v3.

 3. __sub__(self, other): Operator Overloading for Subtraction ➖

Similar to __add__, the __sub__ method overloads the - operator for Vector objects.

1. self: The Vector object on the left side of the subtraction.
2. other: The Vector object on the right side of the subtraction.
3. return Vector(self.x - other.x, self.y - other.y): This creates a new Vector object where the x and y components are subtracted.

How it works: The line v4 = v3 - v1 calls v3.__sub__(v1). The __sub__ method subtracts the components of v1 from the components of v3, yielding a new Vector object (e.g., Vector(6-2, 8-3) = Vector(4, 5)).

 4. __mul__(self, scalar): Operator Overloading for Multiplication (Scalar Multiplication) ✖️

This method enables the use of the * operator with Vector objects, specifically when a Vector is multiplied by a scalar (a simple number).

1. self: The Vector object on the left side of the * operator.
2. scalar: The scalar value (a number) on the right side of the * operator.
3. return Vector(self.x * scalar, self.y * scalar): This creates a new Vector object where each component of the Vector is multiplied by the scalar.

How it works: The line v5 = v1 * 5 calls v1.__mul__(5). The __mul__ method multiplies both the x and y components of v1 by 5, returning a new Vector object (e.g., Vector(2*5, 3*5) = Vector(10, 15)).

Note: If you wanted to do something like 5 * v1 (i.e., the scalar first), you might also need to implement the __rmul__ (right multiply) method. However, for this specific example, __mul__ is sufficient.

 5. __str__(self): String Representation 💬

This method defines what a "user-friendly" string representation of your Vector object should be. It's automatically called when you print an object using the print() function, or when you pass an object to the str() function.

1. self: The Vector object whose string representation is requested.
2. return f"Vector({self.x}, {self.y})": This returns a formatted string using an f-string. Here, {self.x} and {self.y} are replaced with their respective values, resulting in output like Vector(6, 8).

How it works: When you write print(v3), Python internally calls v3.__str__(). This method provides a string (e.g., "Vector(6, 8)") which is then printed to the console. If the __str__ method were not defined, print(v3) would show a default representation that typically includes the object's memory address, which isn't as readable.

Summary:

Dunder methods provide incredible flexibility and control in creating custom data types like the Vector class, allowing your class's objects to interact seamlessly with Python's built-in functions and operators. They make your code more intuitive and "Pythonic," as you can perform operations on your custom objects using familiar operators, just as you would with built-in numbers.


Other common operator overloading methods include:

1. __eq__ (==)

2. __ne__ (!=)

3. __lt__ (<)

4. __gt__ (>)

5. __le__ (<=)

6. __ge__ (>=)

7. __truediv__ (/)

8. __floordiv__ (//)

9. __mod__ (%)

10. __pow__ 

💬💬💬 Explanation:

Dunder methods allow Python classes to mimic the behavior of built-in types when interacting with operators. Here's how the common comparison and arithmetic operator overloading methods work:



 Comparison Operators:

These methods define how objects of your class are compared to each other. They should return a boolean (True or False).

1. __eq__(self, other): Implements the equality operator (==).
    * Explanation: When you use object1 == object2, Python calls object1.__eq__(object2). You'd define this to return True if self is considered equal to other based on your class's logic (e.g., if all their attributes match for Vector objects, both x and y must be the same).

2. __ne__(self, other): Implements the inequality operator (!=).
    * Explanation: When you use object1 != object2, Python calls object1.__ne__(object2). Often, if you implement __eq__, you can simply define __ne__ to return the opposite of __eq__, like return not self.__eq__(other).

3. __lt__(self, other): Implements the less than operator (<).
    * Explanation: When you use object1 < object2, Python calls object1.__lt__(object2). For Vector objects, you might define "less than" based on magnitude, or lexicographically (comparing x first, then y).

4. __le__(self, other): Implements the less than or equal to operator (<=).
    * Explanation: When you use object1 <= object2, Python calls object1.__le__(other). Similar to __lt__, but includes equality.

5. __gt__(self, other): Implements the greater than operator (>).
    * Explanation: When you use object1 > object2, Python calls object1.__gt__(other).

6. __ge__(self, other): Implements the greater than or equal to operator (>=).
    * Explanation: When you use object1 >= object2, Python calls object1.__ge__(other).



 Arithmetic Operators:

These methods define how objects of your class behave with arithmetic operations. They typically return a new object of your class (or another relevant type).

7. __truediv__(self, other): Implements the true division operator (/).
    * Explanation: When you use object1 / object2, Python calls object1.__truediv__(other). For Vector objects, this could mean dividing both x and y components by a scalar or another Vector (if vector division is defined for your context). It typically results in a float.

8. __floordiv__(self, other): Implements the floor division operator (//).
    * Explanation: When you use object1 // object2, Python calls object1.__floordiv__(other). This performs division and rounds down to the nearest whole number (or integer for integer inputs). For Vector objects, this would apply floor division to the components.

9. __mod__(self, other): Implements the modulo operator (%).
    * Explanation: When you use object1 % object2, Python calls object1.__mod__(other). This returns the remainder of a division. For Vector objects, this might mean finding the remainder of x and y components.

10. __pow__(self, other): Implements the exponentiation operator ().
    * Explanation: When you use object1  object2, Python calls object1.__pow__(other). This calculates self raised to the power of other. For a Vector, this could mean raising its magnitude to a power, or applying the power to its components, depending on your mathematical definition for Vector exponentiation.