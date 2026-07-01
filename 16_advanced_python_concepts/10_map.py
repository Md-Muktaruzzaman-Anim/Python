# Rahim's fruit prices
prices = [10, 20, 30, 40, 50]

# Function to double a price
def double_price(price):
    return price * 2

# Using map to double all prices
doubled_prices = list(map(double_price, prices))

# Show result
print("Doubled prices:", doubled_prices)



# Rahim's fruit prices
prices = [10, 20, 30, 40, 50]

# Function to apply 20% discount
def apply_discount(price):
    return price * 0.8  # 20% off means paying 80% of original price

# Using map to apply discount to all prices
discounted_prices = list(map(apply_discount, prices))

# Show result
print("Discounted prices:", discounted_prices)



# num = [1, 2, 3, 45, 4, 21]

# def square(x):
#     return x * x


# new = list(map(square, num))
# print(new)