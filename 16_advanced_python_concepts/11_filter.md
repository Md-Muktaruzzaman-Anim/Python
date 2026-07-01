# I’ll teach you Python’s filter function with a simple example and story, in English, just like I explained map.

1. Story: Rahim, our fruit seller, is working with his fruit price list: 10, 20, 30, 40, 50 taka. Now, he wants to find fruits priced above 30 taka. Checking each price manually wastes time, so he uses Python’s filter function to quickly pick them out!

What is filter?

The filter function selects items from a list that meet a specific condition, making code simple and fast.

# Example Code:

# Rahim's fruit prices
prices = [10, 20, 30, 40, 50]

# Function to check if price is above 30
def is_expensive(price):
    return price > 30

# Using filter to select prices above 30
expensive_prices = list(filter(is_expensive, prices))

# Show result
print("Prices above 30 taka:", expensive_prices)

# Output:

Prices above 30 taka: [40, 50]

# Explanation:

1. prices is Rahim’s list of fruit prices.
2. is_expensive checks if a price is above 30.
3. filter(is_expensive, prices) selects prices where is_expensive returns True.
4. list() converts the result to a list.

Story End: Rahim is delighted! With filter, he quickly found fruits priced above 30 taka. Now, he plans to offer special discounts on these expensive fruits. He’s eager to learn more Python, like how to find cheaper fruits!


# Another e.g.

To help Rahim find cheaper fruits (priced 30 taka or less) and apply special discounts to expensive fruits (above 30 taka) using Python’s filter and map, we’ll extend the story.

**Story Update**: Rahim wants to identify fruits priced 30 taka or less to promote them as budgetriendly. For expensive fruits (above 30 taka), he’ll apply a 10% discount to attract buyers. His price list is [10, 20, 30, 40, 50] taka.

**Example Code**:

# Rahim's fruit prices
prices = [10, 20, 30, 40, 50]

# Filter cheaper fruits (30 taka or less)
def is_cheap(price):
    return price <= 30

cheap_prices = list(filter(is_cheap, prices))
print("Cheaper fruits (≤30 taka):", cheap_prices)

# Apply 10% discount to expensive fruits (>30 taka)
def apply_discount(price):
    return price * 0.9  # 10% off means paying 90% of original price

expensive_prices = list(filter(lambda x: x > 30, prices))  # Filter expensive fruits
discounted_prices = list(map(apply_discount, expensive_prices))  # Apply discount
print("Discounted expensive fruits:", discounted_prices)


**Output**:

Cheaper fruits (≤30 taka): [10, 20, 30]
Discounted expensive fruits: [36.0, 45.0]


**Explanation**:

1. is_cheap checks if a price is 30 taka or less.  
2. filter(is_cheap, prices) selects prices ≤ 30 taka.  
3. For expensive fruits, filter(lambda x: x > 30, prices) selects prices > 30 taka.  
4. apply_discount multiplies by 0.9 (10% off).  
5. map(apply_discount, expensive_prices) applies the discount to expensive fruits.  
6. list() converts results to lists.