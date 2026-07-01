# Class: Class is a blueprint or a template. e.g. Form for an Exam that contains name, age, electives, father's name etc.

# Object: Specific instance created from the template (class), e.g. Form which contains the data for John Doe

class Employee: # This creates a new class called Employee. The class is a blueprint — from which we will later create an employee object.
    company = "hp" # This is a class variable. This means that no matter how many employees are created from this Employee class, they all work in the same company (HP). This variable is shared for all objects.

    def get_salary(self): # This is a method (function inside a class). self means — the object (e1 and e2) that calls it, refers to itself. self is the object's own (current) pointer, through which we access data or methods inside the object.self = the object itself, which is running the method.
        '''Real-life example of self:
Suppose you have a remote control at home to control your TV. Now suppose you have different remotes depending on your TV model — for example, your remote, your father's remote, your mother's remote.
TV = Class (Blueprint)
Remote = Object (Object)
Now when you control your TV with your remote, the TV will know who you are, whose remote you are controlling.
Here self is the remote's own identifier, which tells the TV who is calling.'''
        return 34000 # When this method is invoked, it will return 34000. That is, the salary of this employee is 34,000.
    
e1 = Employee() # Here an object is created from the Employee class — named e1. This is an employee.
print(e1.get_salary()) # This line invokes the get_salary() method of the employee named e1. It will return 34000 and print.
print(e1.company)

e2 = Employee() # Another new employee is created, named e2. This employee is also created from the same class, meaning he works for the same company and has the same salary.
print(e2.get_salary()) # This time the salary of employee e2 will be printed — again 34000.
print(e2.company)


class student:
    school = "Sunrise Public School"

    def grade(self):
        return "A+"
    
s1 = student()
print(s1.school)
print(s1.grade())