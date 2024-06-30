# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

orders = [
('Alice', 'Laptop', 1),
('Bob', 'Camera', 2),
('Jaycob', 'Pajamas', 3),
('Adam', 'TV', 1),
('Cory', 'Shirt', 5)
]

def display_orders():
    print('Customer orders:')

    for i, order in enumerate(orders):
        name, item, quantity = order

        print(f'\nOrder {i + 1}:\n\
Name: {name}\n\
Item: {item}\n\
Quantity: {quantity}')
        
display_orders()