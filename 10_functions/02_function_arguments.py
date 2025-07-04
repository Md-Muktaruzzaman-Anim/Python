    #    Positional Arguments

def add(a, b): # a and b called parameters and these are variable names.
    x = a + b
    return x

c = add(3, 5) # 3 and 5 called arguments. The difference is that 3 and 5 are the real values which are being passed.

print(c)

#    Default Arguments

def add(a, b, plus = 1): # 0 is override by 2. The default value for plus is 1.
    x = a + b + plus
    return x

c = add(3, 5, 2)
print(c)

# e.g.
#         Rules

# def add(a, b=2, c):  # ❌ (SyntaxError)
# def add(a, b, c=2):  # ✅ Right (Default parameters should always be written last:)


# Keyword Arguments

def student(name, age):
    print(f"Name: {name}, Age: {age}")
student(age=20, name="Bob") # Mentioned
student(age=16, name="Anim") # Mentioned

# student(20, "Bob")  # Syntax error
# student(16, "Anim")  # Syntax error