def make_complete_order(*args, **kwargs):
    print("Customer's order:")
    for item in args:
        print(f"- {item}")
    print("\nSpecial instructions:")
    for item, instruction in kwargs.items():
        print(f"{item}: {instruction}")

# Customer's full order
make_complete_order("pizza", "pasta", "burger", pizza="extra cheese", pasta="spicy")