Exception Handling: 'Unexpected Train Errors' 🚂

Imagine you're a skilled train operator. Your job is to safely transport passengers from one station to another. You know that operating a train can present various issues: a tree might fall on the tracks, signals might malfunction, or even the engine could have problems. These problems are what we call 'Exceptions'.

Now, as a good train operator, what would you do? Would you stop the train and sit idly the moment a problem arises, or would you try to solve it? You'd certainly try to solve it!

It's the same in Python. When you write a program, it can encounter various errors during execution. If you can't handle these errors properly, the program will suddenly crash, leading to a very poor user experience.

Exception Handling is the process by which we identify these unexpected errors and write code to safely manage them, preventing the program from crashing.

We use try, except, else, and finally blocks for Exception Handling:

 1.  try block: This block contains the code that is likely to cause an error. Just as a train operator normally drives the train but keeps in mind that danger might arise.

    try:
         Write potentially error-prone code here
        result = 10 / 0  This will raise a ZeroDivisionError
        print(result)
    

 2.  except block: If a specific type of error occurs in the try block, the code in the except block is executed. This is like the train operator taking steps to resolve a problem. If a tree falls on the tracks, the operator arranges to remove it.

    python
    try:
        result = 10 / 0
        print(result)
    except ZeroDivisionError:  When a division by zero error occurs
        print("You tried to divide by zero! This is not possible.")
    except TypeError:  When an error occurs due to incorrect data type
        print("There is a problem with your data type.")
    

    You can use multiple except blocks to handle different types of errors, or simply except Exception as e: to catch any type of error.

 3.  else block: If no error occurs in the try block, the code in the else block is executed. That is, if the train reaches its destination safely, the operator performs their regular duties.

    try:
        result = 10 / 2
        print(result)
    except ZeroDivisionError:
        print("You tried to divide by zero!")
    else:
        print("Calculation successful! No errors occurred.")
    

 4.  finally block: The code in this block is always executed, whether an error occurs or not. Just as a train operator always performs certain tasks (e.g., engine check-up) at the end of the day, regardless of whether the train stops or runs, the finally block works similarly. It's typically used for releasing resources (like closing files).

    try:
        file = open("my_file.txt", "r")
        content = file.read()
        print(content)
    except FileNotFoundError:
        print("The file was not found.")
    finally:
        if 'file' in locals() and not file.closed:  Ensure file is open and not already closed
            file.close()
            print("File closed.")
    



 Custom Errors: 'Your Own Traffic Rules' 🚦

Suppose you are not just a train operator, but also an engineer for the railway company. You've noticed some problems that don't fall under Python's general errors, but are critical for your system. For example, your company has decided that if any train runs more than 30 minutes late, it should be flagged as a serious issue. Python doesn't have a default error that signifies "train 30 minutes late."

What would you do in this case? You'd create your own error\! These self-defined errors are called Custom Errors or User-defined Exceptions.

In Python, we can create our own error classes by inheriting from the Exception class.

class TrainDelayError(Exception):
    """
    This error is raised when a train runs more than 30 minutes late.
    """
    def __init__(self, delay_minutes, message="Train is delayed."):
        self.delay_minutes = delay_minutes
        self.message = f"{message} {delay_minutes} minutes behind schedule."
        super().__init__(self.message) # Call the constructor of the Exception class

# Now, let's use this custom error
def check_train_status(actual_arrival_time, scheduled_arrival_time):
    delay = actual_arrival_time - scheduled_arrival_time
    if delay > 30:
        raise TrainDelayError(delay) # We created our own error
    else:
        print(f"Train is running on time, only {delay} minutes delayed.")

try:
    # Check train arrival time
    check_train_status(100, 50) # Assume here the time difference is 50 minutes
except TrainDelayError as e:
    print(f"Warning: {e.message}")
    print(f"Delay occurred: {e.delay_minutes} minutes.")
except Exception as e: # For any other general error
    print(f"An unexpected error occurred: {e}")


In this example, TrainDelayError is our own custom error. Whenever a train runs more than 30 minutes late, we will raise this TrainDelayError. This will interrupt the normal flow of the program, and we can catch this specific error using an except block and take action accordingly.

Why use Custom Errors?

1.  Clarity: It makes it much clearer what went wrong in your program. Saying "train 30 minutes late" is much clearer than saying "general error."
2.  Control: You have complete control over when and how errors are raised in specific situations within your program.
3.  Structured Handling: Different parts of your program can handle specific custom errors separately, which makes the code more organized.

In summary, Exception Handling is the technique for safely managing unexpected problems in a program, and Custom Errors are your self-named errors to identify specific problems that Python's default error set doesn't cover. Both concepts will help you build more robust, reliable, and user-friendly Python applications. I hope the story helped you understand\!