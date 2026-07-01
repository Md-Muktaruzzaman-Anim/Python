# # Without Walrus operator
# crops = len(['apple', 'banana', 'onion', 'rice'])
# if crops > 3:
#     print(f"{crops} crops, go to market!")
# else:
#     print("Too few crops, no market.")


# With Walrus operator
if (crops := len(['apple', 'banana', 'onion', 'rice'])) > 3:
    print(f"{crops} crops, go to market!")
else:
    print("Too few crops, no market.")



# def very_slow_func():
#     print("Something....")
#     print("Something....")
#     print("Something....")
#     print("Something....")
#     print("Something....")
#     return 7    # Use only one
#     # return 40 # Use only one


# # a = very_slow_func()
# if (a:=very_slow_func()>10):
#     print(a)

# else:
#     print("It's not greater than 10")



while (data:=input('Enter the value: ' )):
       print(data)
       if data == "m":
           break