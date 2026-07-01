class Animal: # Parent class (superclass)
    location = "Bangladesh" # Class variable (one for all Animals).

    def __init__(self, name): # Constructor (To create an Animal, you need to take a name).
        self.name = name # Setting the name variable of the object.
    def speak(self): # Method: Common animal words
        print("Generic animal sound")

class Dog(Animal): # This is how inheritance is done in Python. Dog class, which inherits from Animal
    def speak(self): # Override the speak() method. What's going on here? The Dog class inherits everything from Animal, but rewrites the speak() method in its own way. This is called Method Overriding.
        print("Woof!")

# a = Animal("Dog")
# a.speak()
d = Dog("Tommy") # Create a Dog object (named Tommy).
d.speak() # "Woof!" will print.
print(d.location)
# Since the Dog class has a speak() method, it is invoked, not Animal.



'''
What is super()?
super() is a built-in function in Python,which allows us to call the method or constructor of the parent class from within the child class.

Why is it needed?
Suppose, the Parent class has __init__(),and the Child class writes its own __init__() then if you don't write super().__init__(), the parent's __init__() won't work!
'''

# class Animal:
#     location = "Bangladesh" # Class attribute

#     def __init__(self, name):
#         self.name = name # Instance attribute

#     def speak(self):
#         print("Speaking now....") # Parent class method

# class Dog(Animal): # Inheriting from Animal
#     def speak(self):
#         super().speak() # First call Parent's speak()
#         print("Woof!") # Then my own voice


# a = Animal("Dog")
# a.speak()
# d = Dog("Tommy") # Create an object of Dog class
# d.speak() # Dog's speak() will be called
# print(d.location) # Doing this will print "Bangladesh" (class attribute)


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class student(person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display(self):
        print(f"This is {self.name}, and I am {self.age} years old.,My ID: {self.student_id}")

s1 = student("Muktar", 20,340)
s1.display()

'''What is happening here?
Student is a child class of Person
Student has created its own constructor
But super().__init__(name, age) calls __init__() of Parent class
This sets name and age inside parent'''