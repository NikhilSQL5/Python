"""
WHAT THIS FILE DOES:
Covers Lists, Tuples, Sets, and Dictionaries using E-Commerce business
examples. The for-loop syntax shown here is only a short preview -
Module 7 covers loops in full detail.
"""

# -----------------------------------------------------------------
# Lists - create, access, update, delete
# -----------------------------------------------------------------
order_totals = [7458.30, 4599.00, 1250.50, 4599.00]
print(order_totals)

cities = ["Mumbai", "Delhi", "Bengaluru", "Chennai"]
print(cities[0])     # Mumbai
print(cities[-1])    # Chennai
print(cities[1:3])   # ['Delhi', 'Bengaluru']

cities[0] = "Pune"          # update
cities.append("Kolkata")    # add to the end
print(cities)

cities.remove("Delhi")      # remove by value
print(cities)

# Expected Output:
# [7458.3, 4599.0, 1250.5, 4599.0]
# Mumbai
# Chennai
# ['Delhi', 'Bengaluru']
# ['Pune', 'Delhi', 'Bengaluru', 'Chennai', 'Kolkata']
# ['Pune', 'Bengaluru', 'Chennai', 'Kolkata']
