"""When a function is called in Python (or most programming languages):

1.A new local scope (a temporary memory space) is created for that function.

2. All local variables declared inside that function live in that scope.

3. Once the function finishes executing (returns), that local scope is destroyed, and all local variables are deleted (free from memory).

So yes — variables inside the function are deleted after the function is done. """



# def greet():
#     name = "Alice"
#     print("Hello", name)

# greet()
'''print(name)  # ❌ Error! name is not defined
🔸 name only exists inside the function.
🔸 After greet() finishes, name is destroyed.
🔸 So when we try to print(name) outside, it gives an error.

Question	                                    Answer
1. Do functions keep variables forever?	       ❌ No
2. When are function variables destroyed?	   ✅ After the function returns
3. Where do function variables live?	       ✅ Inside the function's local scope only'''

def sum(a, b):
    # a and b are local variables.
    c = a + b
    z = 1 # It creates a local variable called z which is destroyed after this function returns.
    return c

def greet():
    z = 32 # local variable
    print(("Hello"))

z = 8 # z is a global variable.
print(z)
print(sum(4, 6))
print(z)
