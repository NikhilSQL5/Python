"""
PYTHON OPERATORS

WHAT THIS FILE DOES:
Covers arithmetic, comparison, logical, assignment, membership, and
identity operators using simple E-Commerce business examples.
"""

# -----------------------------------------------------------------
# Arithmetic operators
# -----------------------------------------------------------------

unit_price = 1455.78
quantity = 3

line_total = unit_price * quantity
print("Line total:", line_total)

total_amount = 4599
number_of_orders = 3
average_order_value = total_amount / number_of_orders
print("Average order value:", average_order_value)

# Floor division and modulus - useful for things like "how many full
# boxes of 5 items, and how many are left over"
items_to_ship = 17
items_per_box = 5
full_boxes = items_to_ship // items_per_box
leftover_items = items_to_ship % items_per_box
print("Full boxes:", full_boxes, "| Leftover items:", leftover_items)

# Expected Output:
# Line total: 4367.34
# Average order value: 1533.0
# Full boxes: 3 | Leftover items: 2

# -----------------------------------------------------------------
# Comparison operators
# -----------------------------------------------------------------
order_total = 7458.30

print(order_total > 5000)    # True
print(order_total == 7458.30)  # True
print(order_total != 5000)   # True

status = "Delivered"
print(status == "Cancelled")  # False

# Expected Output:
# True
# True
# True
# False


# -----------------------------------------------------------------
# Logical operators
# -----------------------------------------------------------------
order_total = 7458.30
status = "Delivered"

is_high_value_and_delivered = (order_total > 5000) and (status == "Delivered")
print("High value and delivered:", is_high_value_and_delivered)

is_low_value_or_cancelled = (order_total < 1000) or (status == "Cancelled")
print("Low value or cancelled:", is_low_value_or_cancelled)

print("NOT delivered:", not (status == "Delivered"))

# Expected Output:
# High value and delivered: True
# Low value or cancelled: False
# NOT delivered: False

