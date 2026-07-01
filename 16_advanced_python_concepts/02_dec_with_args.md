First understand that what is nested:

🔍 What does Nested mean?
The word Nested means:

"One inside another"

or
"Something inside"

When we say "Nested Function", "Nested Loop", or "Nested If" in programming, it means:

A function inside another function,
A loop inside another loop,
An if inside another if — etc.

 Example 1: Nested Function (Function inside a function)

def outer():
    print("This is the outer function.")

    def inner():
        print("This is the inner (nested) function.")
    
    inner()

outer()

Explanation:
Here the inner() function is inside the outer() function.

So it is called Nested Function.

 Example 2: Nested If

x = 10

if x > 5:
    print("x is greater than 5")
    if x < 15:
        print("x is also less than 15")

 Here if x < 15: is inside another if
So this is also a Nested If Statement

 Example 3: Nested Loop

for i in range(3):
    print("Outer loop", i)
    for j in range(2):
        print("   Inner loop", j)

for i in range(3):
    print("Outer loop", i)
    for j in range(2):
        print("   Inner loop", j)

...Here for j in range(2) is the inner loop,
which is inside for i in range(3).

When one is inside another, it is called Nested Structure

🧠 Why do we use Nested?

Nested structure helps us to divide our code logically.

In Decorator we use Nested Function because:
1. We create another function inside a function
2. so that we can work on the function (log, repeat, set timer etc.)

What is Nested?                                      Meaning

Nested Function                                      Function inside a function
Nested If                                            if inside an if 
Nested Loop                                          Loop inside a loop 
Nested Dictionary/List                               List inside a list / Dictionary inside a Dictionary


Let's look at the code first:

def repeat(n):                    # (1) Outer function: Takes `n` (number of repetitions)
    def decorator(func):          # (2) Middle function: Takes the original function `func`
        def wrapper(a):           # (3) Inner function: Takes argument `a` for `func`
            for i in range(n):    # (4) Loop `n` times
                func(a)           # (5) Call `func(a)` each time
        return wrapper            # (6) Return the `wrapper` function
    return decorator              # (7) Return the `decorator` function

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")

say_hello("Muktar")

📌 Main target:

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")

say_hello("Muktar")

We want to run the function say_hello("Muktar") 7 times, and we did that with @repeat(7).

 But how does it work?
To understand this, we need to understand:

Decorator with arguments = 3 nested functions

You first have to be patient — I will teach you with an analogy like the one below.

🎓 Imagine you are building a "function wrapping machine"
You are building a machine that you tell —
“Run this function 7 times”
It will understand and run that function 7 times.

To build this machine, you need 3 things:

Step 1: Say from the outside — "Run 7 times"

def repeat(n):

🔹 Here n is the number of times you want to run it — e.g. n = 7

This is your outer function, meaning:

"Create this decorator that will run the function n times"

This returns the inner decorator function.

Step 2: Give the function to run

def decorator(func):

🔹 Here func is the function you want to repeat
 For example: say_hello

The function hasn't been executed yet — it's just the function.

Step 3: Now create a wrapper that will do the work

def wrapper(a):
    for i in range(n):
        func(a)

🔹 Here wrapper is the function that will actually run say_hello("Muktar") repeatedly.

 a is the name you are sending (e.g. "Muktar")

 The loop will run n times (7 times)

 Each time func(a) will be called = say_hello("Muktar")

All functions are nested: (structure)

def repeat(n):          # Takes your input — how many times to run
    def decorator(func):     # Takes your main function
        def wrapper(a):           # Creates a new function that runs the main function
            for i in range(n):
                func(a)
        return wrapper
    return decorator

 Now if you write:

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")

This is exactly like this:

def say_hello(a):
    print(f"Hello! {a}")

say_hello = repeat(7)(say_hello)

 You first call the outer function with repeat(7)
 Then the say_hello function goes into decorator(func)
 wrapper(a) is created
 Now say_hello = wrapper

🎬 Now when you say:

say_hello("Muktar")

 Then wrapper("Muktar") is called

 Which runs say_hello("Muktar") 7 times

🧠 The whole process is like a short story:
1. You say: "Run this function 7 times" → @repeat(7)
2. Your say_hello() function is packed
3. A new wrapper() is created which runs say_hello() 7 times
4. Then when you call say_hello("Muktar"),
➤ That new wrapper() is run
➤ Which prints Hello! Muktar 7 times

Final output:
          Hello! Muktar
          Hello! Muktar
          Hello! Muktar
          Hello! Muktar
          Hello! Muktar
          Hello! Muktar
          Hello! Muktar


🔚 Trick to understand:
Part                                 Means
repeat(n)                            configures how many times to run
decorator(func)                      which function to run
wrapper(a)                           actually does the work of running

📌📌📌 I explain these more deeply:

🧱 Let's break it down into 3 steps:
STEP 1: What does @repeat(7) mean?
When you write @repeat(7), Python converts it as follows:

say_hello = repeat(7)(say_hello)

There are 2 things going on here:

repeat(7)
 This is a function call, where you say:
"I need to run my function 7 times".
👉 The repeat(n) function creates a decorator and returns

STEP 2: Now what is happening inside repeat(7)?

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

What's happening here:

Function work
repeat(n) tells you how many times you want to run the function
decorator(func) takes the actual function
wrapper(a) runs the function n times

🔍 The inner process step by step:
Step 1: You write @repeat(7)
Python sees this and calls repeat(7)

It assumes n = 7

decorator = repeat(7)

Step 2: Now Python passes the say_hello function to the decorator function:
say_hello = decorator(say_hello)

 Now the say_hello function is no longer the same as before, it is now a new function called wrapper().

Step 3: wrapper(a) is created:
def wrapper(a):
    for i in range(n):
        func(a)

1. Here func is say_hello
2. and n = 7
3. so func(a) → say_hello("Muktar") → will run 7 times

Now when you say:
say_hello("Muktar")

 It looks like you are calling say_hello
 But actually you are calling wrapper("Muktar")
 Which runs say_hello("Muktar") 7 times

 It will be easier to understand with the image:

        YOU                 DECORATOR SYSTEM

    say_hello("Muktar")  ──────────────▶ wrapper("Muktar")
                                   ┌─────────────┐
       say_hello("Muktar") ◀──────│  func(a)     │
       say_hello("Muktar") ◀──────│  func(a)     │
       say_hello("Muktar") ◀──────│  func(a)     │
       say_hello("Muktar") ◀──────│  func(a)     │
       say_hello("Muktar") ◀──────│  func(a)     │
       say_hello("Muktar") ◀──────│  func(a)     │
       say_hello("Muktar") ◀──────│  func(a)     │
                                   └─────────────┘

🧠 Why are we getting so complicated?
Because we want flexibility. We want the function to repeat, log, authorize, retry, etc. —
but not change the original function, but work around it.
This is called “Decorating” a function.

 Now if you want to make it more complicated:
If the function has more than 1 argument:

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):   # Any number of inputs
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name, msg):
    print(f"{msg}, {name}!")

greet("Muktar", "Good Morning")

📤 output:

Good Morning, Muktar!
Good Morning, Muktar!
Good Morning, Muktar!

If a return value is needed:
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

🔚 Summary:
Point                       Explanation

@repeat(7)                  outer function — tells how many times to run.
decorator(func)             gets the function, which is to be repeated.
wrapper(a)                  new function — which actually does the job.
Result                      say_hello("Muktar") → runs 7 times.