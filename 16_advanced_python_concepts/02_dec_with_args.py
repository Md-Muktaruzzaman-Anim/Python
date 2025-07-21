def repeat(n):                    # Takes your input — how many times to run.
    def decorator(func):          # Takes your main function
        def wrapper(a):           # Inner function: Takes argument `a` for `func`.Creates a new function that runs the main function
            for i in range(n):    # Loop `n` times
                func(a)           # Call `func(a)` each time
        return wrapper            # Return the `wrapper` function
    return decorator              # Return the `decorator` function

@repeat(7)
def say_hello(a):
    print(f"Hello {a}")

say_hello("World!")

x = 10

if x > 5:
    print("x is greater than 5")
    if x < 15:
        print("x is also less than 15")