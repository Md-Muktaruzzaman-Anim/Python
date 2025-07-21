from functools import reduce  # Import reduce function

# Rahim's fruit prices
prices = [10, 20, 30, 40, 50]

# Function to add two prices
def add_prices(a, b):
    return a + b

# Using reduce to sum all prices
total_price = reduce(add_prices, prices)

# Show result
print("Total price of all fruits:", total_price)



# from functools import reduce

# numbers = [1, 2, 3, 4, 5, 6]
# #         [3, 3, 4, 5, 6]
# #         [6, 4, 5, 6]
# #         [10,5, 6]
# #         [15,6]
# #         [21]

# def sum(a, b):
#     return a + b

# c = reduce(sum, numbers)
# print(c)