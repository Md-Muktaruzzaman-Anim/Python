⁂⁂⁜⁜ Object-Oriented Programming, or OOP for short, is a programming approach where we translate real-life thinking into code. We see everything as objects.

These objects are created from a class, which is like a blueprint or design.

🎯 Real-life Example:
Imagine you design a car. That design is the Class.
Now, if you build an actual car using that design — that is the Object.

🔹 Class = Design / Blueprint
🔹 Object = Real item built from that design

1. Encapsulation
Definition:
Encapsulation is the practice of bundling data and functions together inside a class, so that external access to the internal data is restricted.
For example, __balance cannot be accessed directly from outside. That’s encapsulation. 🔒

🧺 Real-life Example:

Juice carton or bottle

When you drink juice, you just open the bottle and drink.
You don’t know or need to know how the juice was made or how much water was added.

1.1 The contents of the bottle are hidden (Encapsulated).
1.2 You just use the necessary part (drinking the juice).

1.3 Similarly, in programming, we keep data/methods inside a class and prevent direct access from the outside.

2. Inheritance
Definition:
Inheritance means one class (Child/Derived class) receives the properties and behaviors of another class (Parent/Base class).

🧬 Real-life Example:
Human and child

You inherit some features (like eye color, height, behavior) from your parents.
You can also add new traits of your own (like musical talent).

2.1 Just like a child inherits traits from parents, a class in programming inherits from another class.

2.2 In Python, one class can receive properties and methods from another class — this is called inheritance.

3. Polymorphism
Definition:
Polymorphism means the same function/method name can behave differently in different contexts.

🐾 Real-life Example:
The word "cholo" (let’s go)

“Let’s go to school.”

“The car is moving.”

“The bird flew away.”

Here, the same word "cholo" is used in different senses.
3.1 This is Polymorphism — same name, different behavior.

3.2 In Python, the same method or function name can work differently across different classes.

4. Abstraction
Definition:
Abstraction means showing only the necessary details and hiding the complex internal parts.

In Python, to create abstract classes, we use the abc (Abstract Base Class) module.

🚗 Real-life Example:
Driving a car

When you drive a car, you:

Hold the steering wheel

Press the brake

Shift gears

But you don’t know (and don’t need to know) how the engine works internally, how the pistons move, etc.

4.1 You only use what you need — the complex internals are hidden.

4.2 In Python, we use abstract classes to show only the required methods — the rest of the implementation stays hidden.