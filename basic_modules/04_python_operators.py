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

