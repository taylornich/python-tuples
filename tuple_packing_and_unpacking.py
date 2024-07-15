# question 3 task 1

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2)
]

index = 0

for order in orders:
    name, item, quantity = order
    print(f"Order #{index + 1}:")
    print(f"Name: {name}")
    print(f"Item Ordered: {item}")
    print(f"Quantity Ordered: {quantity}")
    index += 1