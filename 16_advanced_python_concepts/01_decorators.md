Decorators:

Python decorators are a very powerful and magical feature that allows you to add new features to a function without changing the original function.

In simple terms: What is a Decorator?
1. Suppose you have a function that does something.
2. Now you want to do some extra work before or after that function runs — like logging, timing, authorizing, etc.

⁂⁂ This is where decorators come in handy —
"wrapping extra features around the function without changing the function!"

🧩 In a decorator, the wrapper function is an inner function that:

"Wraps" (modifies/extends) the original function (func).

Controls when and how the original function is called.

Can add extra logic (e.g., logging, timing, authentication) before/after calling func.

🧩 How wrapper Works in a Decorator?

1. Basic Structure of a Decorator

def decorator(func):        # Takes a function (e.g., `greet()`)
    def wrapper():          # Inner function that modifies `func`
        print("Before calling func")  # Extra logic
        func()              # Calls the original function
        print("After calling func")   # Extra logic
    return wrapper          # Returns the modified function

@decorator
def greet():
    print("Hello!")

greet()  # Calls `wrapper()`, which wraps `greet()`

output:
       Before calling func  
       Hello!  
       After calling func  

2. Why Use wrapper?
Extends functionality without modifying the original function.

Preserves the original function (func) and adds new behavior around it.

Flexible: Can accept arguments (*args, **kwargs) if needed.

Main Points:
1. The heart of the wrapper decorator – it wraps the original function and adds extra logic.
2. Using *args, **kwargs will work in any function.
3. Widely used in web frameworks (Flask, Django) (routing, authentication, etc.).


✨ Let's look at the code first:

def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return wrapper

 This is the decorator function
🔍 Line-by-line explanation:

🔹 def decorator(func):
Here, a function named decorator is being defined, which takes another function as an argument.
 This is a Higher-Order Function because it takes another function as input.
Here, func will be any function that we want to "decorate".

🔹 def wrapper():
Inside this line, we are creating another new function called wrapper.
 This wrapper() function acts like a "wrap" or "cover" around the main function.

🔹 print("I am about to execute a function....")
Here, the decorator performs some work before the main function—this is a pre-processing step.
Meaning: It says something before executing the function.

🔹 func()
Here, func() is the original function that we have wrapped with the decorator.
 For example, in our case, func refers to the say_hello function.

🔹 print("I have executed this function....")
Here, the decorator performs some work after the main function—this is a post-processing step.
Meaning: It says something after executing the function.

🔹 return wrapper
Here, the decorator() function returns the wrapper function.
 Important Note: We write wrapper (not wrapper()) because we are returning a reference to the function, not calling it.

🔹 Key Points:
Decorator → A function that takes another function and extends its behavior.

Wrapper → The inner function that "wraps" the original function.

Pre/Post Processing → Code that runs before/after the main function.

Returning wrapper (not wrapper()) → Ensures the function is returned for later execution, not called immediately.

🧪 Now let's look at the following part:

def say_hello():
    print("Hello!")
This is our simple function — one that just prints “Hello!”

f = decorator(say_hello)

What's going on here?

1. We're passing the say_hello function to the decorator() function.
2. When we call decorator(say_hello), it goes inside and creates a new function called wrapper.
3. It returns that wrapper function, and we're putting that in the variable f.

Now running f() means running the wrapper() function!

 What happens when we run f():
f()
 The output will be as follows:

I am about to execute a function....
Hello!
I have executed this function....

📌 Summary:
1. A decorator is a function that wraps around another function, either before or after it.
2. It allows you to change or extend the behavior of the original function without touching it.
3. This is called “function manipulation” or wrapping the function.


f will look like this
def f()
      print("I am about to execute a function....")
      print("Hello!")
      print("I have executed this function....")

✨ The f() function essentially does 3 things:

1. First prints "I am about to execute a function...."

2. Then prints "Hello!" (the main function's job)

3. Finally prints "I have executed this function...."

When using a decorator:
We split the same work into two separate functions:

1. say_hello() - Only handles the core functionality (printing "Hello!")

2. decorator() - Adds the extra "wrapping" functionality (before/after messages)

✨✨Comparison Table:

Direct Function(f)	                                  Using Decorator
All code in one function	                          Work divided into two functions
Less reusable	                                      More reusable and modular
Harder to maintain	                                  Easier to maintain and modify
All logic mixed together	                          Core logic separated from additional behavior
Key Benefits of Decorators:
Separation of Concerns - Keeps core functionality clean

Reusability - Same decorator can be used on multiple functions

Flexibility - Can easily add/remove behavior without changing core function

Readability - Makes code organization clearer

Both approaches give the same output, but the decorator version is more maintainable and professional!

"
def f():
    print("I am about to execute a function....")
    print("Hello!")
    print("I have executed this function....")

f()
"

"
def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return wrapper

def say_hello():
    print("Hello!")

f = decorator(say_hello)
f()
"

Where decorators work:

1. Code is modular
2. Additional work can be added before/after any function without repeating code
3. Code is easier to maintain


🔹🔹🔹 1. What does @decorator do?
This line:

@decorator
def say_hello():
    print("Hello!")
This is actually Python's shortcut syntax. It is actually equivalent to the following code:

def say_hello():
    print("Hello!")

say_hello = decorator(say_hello)

📌 So @decorator means:
 Pass the function named say_hello to the decorator() function
 Then set the return value back to say_hello

 So what's happening now?
➤ say_hello() is basically this function:
def say_hello():
    print("Hello!")

 But with @decorator, this is what happens:

say_hello = decorator(say_hello)

And we had the decorator() function:

def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("I have executed this function....")
    return wrapper

So when say_hello was sent, func = say_hello
and the decorator returned the wrapper() function.
Now say_hello means the wrapper() function!

🔹 2. What is say_hello() now?
If you now write:
say_hello()

So you are actually calling the wrapper() function, because say_hello = wrapper.

📤 Then the output is:
I am about to execute a function....
Hello!
I have executed this function....

🧠 Now the whole flow is in one line:
Steps                                 Task

Step 1                                The say_hello() function is created
Step 2                                @decorator passes it to decorator(say_hello)
Step 3                                Inside decorator(), wrapper() is created and returns it
Step 4                                say_hello = wrapper
Step 5                                When say_hello() is called, wrapper() is called, which runs say_hello() from within

🔍 One-line summary:
@decorator is used to wrap functions — so you can do some extra work before or after the main function, without changing the code.