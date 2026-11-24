"""
WHAT THIS FILE DOES:
Covers string creation, indexing, slicing, string methods, f-strings,
and text-cleaning examples using E-Commerce business data.
"""

# -----------------------------------------------------------------
# Creating strings
# -----------------------------------------------------------------
city = "Mumbai"
product_name = "Wireless Earbuds"
email = "nick@example.com"

print(city)
print(product_name)
print(email)

# -----------------------------------------------------------------
# String indexing
# -----------------------------------------------------------------
product_name = "Earbuds"
print(product_name[0])    # E  (first character)
print(product_name[3])    # b
print(product_name[-1])   # s  (last character, using negative indexing)

# Expected Output:
# E
# b
# s

# -----------------------------------------------------------------
# String slicing
# -----------------------------------------------------------------
email = "nick@example.com"
username_part = email[0:12]
print(username_part)   # nick

product_name = "Wireless Earbuds"
print(product_name[:8])    # Wireless
print(product_name[9:])    # Earbuds

# Expected Output:
# nick
# Wireless
# Earbuds

# -----------------------------------------------------------------
# String methods
# -----------------------------------------------------------------
status = "delivered"
print(status.upper())          # DELIVERED

raw_city = "  Mumbai  "
print(raw_city.strip())        # Mumbai (no extra spaces)

raw_payment = "COD"
print(raw_payment.replace("COD", "Cash on Delivery"))  # Cash on Delivery

full_name = "nick"
print(full_name.title())       # nick 

csv_line = "nick,Mumbai"
parts = csv_line.split(",")
print(parts)                   # ['nick', 'Mumbai']

print(len("Earbuds"))          # 7
print("Delivered".startswith("Del"))  # True
print("Delivered".endswith("ed"))     # True

"""
Problem Statement
A shop keeps a set of active customer IDs. Add customers, remove customers, and see the difference between remove() and discard().

Example Input
active_customers = {"C101", "C102", "C103"}

Expected Output
After add: ['C101', 'C102', 'C103', 'C104']
After adding C101 again: ['C101', 'C102', 'C103', 'C104']
After update: ['C101', 'C102', 'C103', 'C104', 'C105', 'C106']
After remove: ['C101', 'C103', 'C104', 'C105', 'C106']
After discard of a missing ID: ['C101', 'C103', 'C104', 'C105', 'C106']
remove() raised a KeyError for C999


"""

active_customers = {"C101", "C102", "C103"}

active_customers.add("C104")
print("After add:", sorted(active_customers))

active_customers.add("C101")
print("After adding C101 again:", sorted(active_customers))

active_customers.update(["C105", "C106"])
print("After update:", sorted(active_customers))

active_customers.remove("C102")
print("After remove:", sorted(active_customers))

active_customers.discard("C999")
print("After discard of a missing ID:", sorted(active_customers))

try:
    active_customers.remove("C999")
except KeyError:
    print("remove() raised a KeyError for C999")

