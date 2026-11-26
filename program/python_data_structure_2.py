"""
A shop saves the stock of each product in a dictionary. List the products, list the stock numbers, find the products that need reordering (stock below 20), count the total units, and check some products.

Example Input
stock = {"Pen": 100, "Notebook": 40, "Bag": 15, "Marker": 0}

Expected Output
Products: ['Pen', 'Notebook', 'Bag', 'Marker']
Stock numbers: [100, 40, 15, 0]
Products to reorder:
  Bag has only 15 units
  Marker has only 0 units
Total units: 155
Is Pen in stock list? True
Is Tablet in stock list? False

"""

stock = {"Pen": 100, "Notebook": 40, "Bag": 15, "Marker": 0}

print("Products: ", list(stock.keys()))

print("Stock numbers: ", list(stock.values()))

print("product to reorder: ")
for product, unit in stock.items():
    if unit < 20:
        print(" ", product, " has only ", unit, " units.")

print("Total units: ", sum(stock.values()))

print("Is Pen in stock list? ", "Pen" in stock)

print("Is Tablet in stock list? ", "Tablet" in stock)
