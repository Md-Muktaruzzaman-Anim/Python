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