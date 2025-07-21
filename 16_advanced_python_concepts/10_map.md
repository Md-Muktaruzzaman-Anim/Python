Story: Rahim, a fruit seller, has fruits priced at 10, 20, 30, 40, and 50 taka. He wants to double each price due to a market hike but doesn’t want to calculate manually. He uses Python’s map function to double all prices at once!

What is map?

The map function applies a given function to each item in a list, returning new results. It’s fast and simplifies code.

Example Code:

# Rahim's fruit prices
prices = [10, 20, 30, 40, 50]

# Function to double a price
def double_price(price):
    return price * 2

# Using map to double all prices
doubled_prices = list(map(double_price, prices))

# Show result
print("Doubled prices:", doubled_prices)


# Output:

Doubled prices: [20, 40, 60, 80, 100]

# Explanation:

1. prices is the list of fruit prices.
2. double_price multiplies each price by 2.
3. map(double_price, prices) applies double_price to each price.
4. list() converts the result to a list.

Story End: Rahim is happy! Doubling prices was quick, thanks to map. Now he wants to learn Python for more complex tasks like discounts!


# Another e.g.

To help Rahim apply discounts using Python’s map function, we’ll extend the story. Suppose Rahim wants to give a 20% discount on each fruit price (originally 10, 20, 30, 40, 50 taka) to attract more customers.

# Example Code:

# Rahim's fruit prices
prices = [10, 20, 30, 40, 50]

# Function to apply 20% discount
def apply_discount(price):
    return price * 0.8  # 20% off means paying 80% of original price

# Using map to apply discount to all prices
discounted_prices = list(map(apply_discount, prices))

# Show result
print("Discounted prices:", discounted_prices)

# Output:

Discounted prices: [8.0, 16.0, 24.0, 32.0, 40.0]

# Explanation:

1. prices is Rahim’s list of fruit prices.
2. apply_discount multiplies each price by 0.8 (100% - 20% = 80%).
3. map(apply_discount, prices) applies the discount to each price.
4. list() converts the result to a list.