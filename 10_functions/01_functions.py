# a = 4
# b = 2
# c = 1

# average = (a + b + c)/3.0
# print(average)

# a1 = 6
# b1 = 12
# c1 = 7

# average1 = (a1 + b1 + c1)/3
# print(average1)

#    Positional Arguments

def average(a, b, c): # This is a function called average and in order to create a function in python we can use def keyword
    d = (a + b + c)/3.0

    # print(d) # 1. Work: It only shows (displays) output to the console. #2. Memory: Does not return a value, so cannot be stored in another variable. # 3. Use case: For debugging or to show results to the user.

    return d # 1. Work: Sends the value out of the function (for storage/reuse).# 2. Memory: The value is returned, so it can be stored in another variable.# 3. Use case: To use the result of the function elsewhere.

o1 = average(3, 5, 1)
o2 = average(3, 6, 9)
o3 = average(10, 10, 10)

print(o1)
print(o2)
print(o3)