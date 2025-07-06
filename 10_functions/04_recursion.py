"""
0 1 1 2 3 5 8 13 21
0 1 2 3 4 5 6  7  8 .....index

fib(0) = 0
fib(1) = 1
fib(2) = fib(1) + fib(0) = 1 + 0 = 1
fib(3) = fib(2) + fib(1) = 1 + 1 = 2
fib(4) = fib(3) + fib(2) = 2 + 1 = 3
fib(5) = fib(4) + fib(3) = 3 + 2 = 5
 
fib(n) = fib(n-2) + fib(n-1) #To find the (n)th number in the Fibonacci series, you need to add the previous two numbers.

                 SUMMARY

Topic                        Explanation

1.Fibonacci Series             Each number = sum of the previous two numbers
2.Base Case                    fib(0) = 0, fib(1) = 1
3.Recursive Formula            fib(n) = fib(n-1) + fib(n-2)
4.Problem                      Too many recalls (slow)
5.Solution                       Using Memoization or Loop
"""



def fib(n):
    # Base case of recusion
    if(n == 0 or n == 1): # This becomes false because n = 6
       return n

    return fib(n-2) + fib(n-1)

# fib(n) = value of the (n)th index of the Fibonacci series
print(fib(6))

# Recursively calling like this:

fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(3) + fib(5)
0 + 1 + fib(1) + fib(2) + fib(3) + fib(4)
0 + 1 + 1 + fib(0) + fib(1) + fib(1) + fib(2) + fib(4)
0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 +1