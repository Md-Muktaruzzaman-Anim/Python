def make_food_order(*args):
    print("Customer's order:")
    for item in args:
        print(f"- {item}")

# Customer's order
make_food_order("pizza", "pasta", "burger")