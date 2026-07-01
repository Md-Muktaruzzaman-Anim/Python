Operator Overloading:

Operator Overloading means making operators (like +, -, *, /, == etc.) work in their own way for a class. That is, we can redefine common operators so that they work specifically for the objects we create.

Let's understand with a real-world example:
Suppose you have a class called "Point" through which you create 2D points (x, y). Now you want to add two points (+) to add their x and y separately. Normally the + operator does not know such a thing, but using Operator Overloading you can do this.


Part	                               Explanation

self	                               The current object (p1) — the object from which sum() is called
p	                                   The other point object (e.g., p2) that needs to be added to self
self.x + p.x	                       p1.x + p2.x → Adds the x-coordinates
self.y + p.y	                       p1.y + p2.y → Adds the y-coordinates
Point(...)	                           Creates a new point and returns it

Explanation with examples:
p1 = Point(3, 2)  # p1.x = 3, p1.y = 2
p2 = Point(6, 3)  # p2.x = 6, p2.y = 3

result = p1.sum(p2)

Here p1.sum(p2) says:
"p1 you add p2 to yourself to get a new point."

Then this part will run:
return Point(self.x + p.x, self.y + p.y)
# return Point(3 + 6, 2 + 3)
# return Point(9, 5)
Now the value of result is → x = 9, y = 5

1. Real example (think simple):
Let's say p1 is: If you walk 3 steps forward, 2 steps right, where will you go.
p2 is: If you walk 6 steps forward, 3 steps right, where will you go.
Then p1 + p2 means: In total, 9 steps forward, 5 steps right.

In one line summary:
sum() method → Adds x and y of two points separately and creates a new Point.

understand Operator Overloading line by line with code:

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2) # Returns a new point which is sum of p1 and p2
p = p1 + p2 # We overloaded the + Operator by writing __add__ function
p.print_point()


Explanation:

Objective of the code:
We are creating a class called Point, which represents a point in a 2D coordinate system.
With this class we can:

1. Create a point (x, y)
2. Create a new point by joining two points
3. Print the x and y of the point nicely

🔶 Step-by-step Explanation:

 ✅ Step 1: Class definition
 class Point:
With this, we are creating a class — Point, which is a blueprint or design, with which many points can be created.

✅ Step 2: Constructor → __init__ method
    def __init__(self, x, y):
        self.x = x
        self.y = y
What is happening in this part:

1. __init__ is the constructor, which is automatically executed when the object is created.
2. Here it takes two parameters named x and y.
3. self.x = x → means that a variable named x is created in this object and it is set with the value of the parameter x.
4.Similarly, self.y = y is set.
🧠 Remember: self means this object, which we are creating.

✅ Step 3: sum() method
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))

This is a function (method) where:

1. self is p1 (from which the method is being called)

2. p is p2 (the other point to be added to)

Now:
self.x = 3
p.x = 6
→ self.x + p.x = 9

self.y = 2
p.y = 3
→ self.y + p.y = 5
Then it takes this new x=9, y=5 and creates a new point called Point(9, 5) and returns it.

✅ Step 4: print_point() method
    def print_point(self):
        return print(f"X is {self.x} and Y is {self.y}")
This is:
1. A method to print the x and y values of a point in a nice way.
2. It uses f-strings to directly output:
👉 X is 9 and Y is 5

✅ Step 5: Create Object
p1 = Point(3, 2)
p2 = Point(6, 3)
Here are two point objects created:

p1.x = 3, p1.y = 2
p2.x = 6, p2.y = 3

✅ Step 6: Adding points
p = p1.sum(p2)
Here p1.sum(p2) means:

1. Add x of p1 and x of p2 → 3 + 6 = 9
2. Add y of p1 and y of p2 → 2 + 3 = 5

➡️ Now a new point p is created:
p.x = 9, p.y = 5

✅ Step 7: Print Output
p.print_point()

When this is called, the print_point() method is executed, and the output is:

Output: X is 9 and Y is 5

Remember:

Object                                     Explanation

self	                                   This object refers to
__init__	                               When an object is created, it is automatically.
Point(...)	                               Used to create a new object                  
method	                                   Function inside the class
p1.sum(p2)	                               Creates a new point by adding two points

🎁 Bonus Idea:
If you want, you can now make it a little more interesting by adding the following features:

__str__() → so that it looks nice when you print(p)

__add__() → so that points can be added by just p1 + p2

distance_to() → to find the distance between two points