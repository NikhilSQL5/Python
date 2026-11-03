"""
PYTHON FUNDAMENTALS
Practical File

WHAT THIS FILE DOES:
Covers variables, comments, data types, type(), type conversion,
print() and input() - all using simple E-Commerce business examples.
No Pandas yet. Just plain Python.
"""

# -----------------------------------------------------------------
# STEP 1: Creating variables
# -----------------------------------------------------------------
# A variable stores a single piece of information.

customer_name = "Nick"
city = "Mumbai"
order_total = 7458.30
number_of_items = 3
is_delivered = True

print(customer_name)
print(city)
print(order_total)
print(number_of_items)
print(is_delivered)

# Expected Output:
# Nick
# Mumbai
# 7458.3
# 3
# True


# -----------------------------------------------------------------
# STEP 2: Comments
# -----------------------------------------------------------------
# Anything after a # is ignored by Python. Use comments to explain WHY.

# This variable stores the customer's total order value in INR
order_total = 7458.30  # inline comment example


# -----------------------------------------------------------------
# STEP 3: Checking data types with type()
# -----------------------------------------------------------------

print(type(customer_name))     # <class 'str'>
print(type(order_total))       # <class 'float'>
print(type(number_of_items))   # <class 'int'>
print(type(is_delivered))      # <class 'bool'>


# -----------------------------------------------------------------
# STEP 4: Type conversion
# -----------------------------------------------------------------
# Data from files or user input often arrives as text (string) even
# when it represents a number. We must convert it before doing math.

quantity_text = "3"                     # this is a STRING, not a number
quantity_number = int(quantity_text)    # now it is an INTEGER

price_text = "1455.78"
price_number = float(price_text)        # now it is a FLOAT

total_value = quantity_number * price_number
print("Total value:", total_value)

# Expected Output:
# Total value: 4367.34


# -----------------------------------------------------------------
# STEP 5: Converting a number back to a string
# -----------------------------------------------------------------
# Useful when building a text message that includes a number.

order_id = 105
message = "Order number " + str(order_id) + " has been placed."
print(message)

# Expected Output:
# Order number 105 has been placed.

# NOTE: print(message) works without str() too if you separate values
# with commas, e.g. print("Order number", order_id, "has been placed.")
# str() is required only when you JOIN text using the + operator.


# -----------------------------------------------------------------
# STEP 6: Using input() to collect data
# -----------------------------------------------------------------
# input() pauses the program and waits for the user to type something.
# Uncomment the two lines below to try it yourself.

# entered_city = input("Enter customer city: ")
# print("You entered:", entered_city, "| Type:", type(entered_city))

# NOTE: input() ALWAYS returns a string, even if the user types a number.
# Example: if the user types 25, entered_age = input(...) stores "25" (string),
# not 25 (integer). Convert it with int() if you need to do math with it.


# -----------------------------------------------------------------
# BUSINESS EXAMPLE: A simple order summary
# -----------------------------------------------------------------
customer_name = "Nick"
city = "Mumbai"
order_total = 7458.30
number_of_items = 3
is_delivered = True

print("----------------------------------------")
print("ORDER SUMMARY")
print("----------------------------------------")
print(customer_name, "from", city, "spent", order_total)
print("Items:", number_of_items, "| Delivered:", is_delivered)

# Expected Output:
# ----------------------------------------
# ORDER SUMMARY
# ----------------------------------------
# Nick from Mumbai spent 7458.3
# Items: 3 | Delivered: True

print("Practical complete.")
