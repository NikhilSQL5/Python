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
