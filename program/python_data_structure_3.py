"""
Problem Statement
Count how many times each word appears in a customer review. Ignore capital letters.

Example Input
review = "Good product good price Fast delivery GOOD quality fast support"

Expected Output
good : 3
product : 1
price : 1
fast : 2
delivery : 1
quality : 1
support : 1

"""

review = "Good product good price Fast delivery GOOD quality fast support"
words = review.lower().split()

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1 #word_count.get(word, 0) gives the current count, or 0 if the word is new. Adding 1 updates the count.

for word in word_count:
    print(word, ":", word_count[word])

"""
Problem Statement
A list has sales records as (product, sales amount). Calculate the total sales of each product and find the highest-selling product.

Example Input
sales = [
    ("Pen", 1000), ("Bag", 3000), ("Notebook", 2000), ("Pen", 1500),
    ("Bag", 1800), ("Notebook", 800), ("Pen", 500)
]

Expected Output
Total sales by product:
  Pen : 3000
  Bag : 4800
  Notebook : 2800
Highest-selling product: Bag ( 4800 )

"""

sales = [
    ("Pen", 1000), ("Bag", 3000), ("Notebook", 2000), ("Pen", 1500),
    ("Bag", 1800), ("Notebook", 800), ("Pen", 500)
]

total_products = {}

for product, price in sales:
    total_products[product] = total_products.get(product, 0) + price

print("Total sales by product: ")
for products in total_products:
    print(" ", products, " : ", total_products[product])

best_product = ""
best_price = 0

for product, price in total_products.items():
    if price > best_price:
        best_product = product
        best_price = price

print("Highest-selling product: ", best_product, "(",best_price,")")


