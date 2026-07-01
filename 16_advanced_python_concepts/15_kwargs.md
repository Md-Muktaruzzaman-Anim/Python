# **kwargs: When Customers Give Special Instructions

Now, a customer says, "Extra cheese on pizza, spicy pasta, less mayo on burger." **kwargs handles these named instructions.

# Code:

def make_food_order_with_instructions(**kwargs):
    print("Customer's special instructions:")
    for item, instruction in kwargs.items():
        print(f"{item}: {instruction}")

# Customer's order
make_food_order_with_instructions(
    pizza="extra cheese", 
    pasta="spicy", 
    burger="less mayo"
)

# Output:

Customer's special instructions:
pizza: extra cheese
pasta: spicy
burger: less mayo

# Explanation: 
**kwargs is another basket, but for named items. Each food item is paired with its instruction, like pizza="extra cheese".