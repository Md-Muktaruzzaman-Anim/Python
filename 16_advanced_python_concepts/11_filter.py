# Rahim's fruit prices
prices = [10, 20, 30, 40, 50]

# Function to check if price is above 30
def is_expensive(price):
    return price > 30

# Using filter to select prices above 30
expensive_prices = list(filter(is_expensive, prices))

# Show result
print("Prices above 30 taka:", expensive_prices)



# # Rahim's fruit prices
# prices = [10, 20, 30, 40, 50]

# # Filter cheaper fruits (30 taka or less)
# def is_cheap(price):
#     return price <= 30

# cheap_prices = list(filter(is_cheap, prices))
# print("Cheaper fruits (≤30 taka):", cheap_prices)

# # Apply 10% discount to expensive fruits (>30 taka)
# def apply_discount(price):
#     return price * 0.9  # 10% off means paying 90% of original price

# expensive_prices = list(filter(lambda x: x > 30, prices))  # Filter expensive fruits
# discounted_prices = list(map(apply_discount, expensive_prices))  # Apply discount
# print("Discounted expensive fruits:", discounted_prices)



# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
    
# a = [1, 3, 5, 7, 9, 54, 657, 321, 220, 350]

# new = list(filter(is_greater_than_9, a))

# print(new)