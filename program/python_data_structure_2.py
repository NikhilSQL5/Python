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

"""
Create the same numbers in a list, a tuple and a set, and a small dictionary. Show how they treat duplicates, how they can be changed, and how you read items from them.

Example Input
values: 10, 20, 20, 30

Expected Output
List: [10, 20, 20, 30] length 4
Tuple: (10, 20, 20, 30) length 4
Set: [10, 20, 30] length 3
Dictionary: {'Pen': 10, 'Bag': 600} length 2
List after append: [10, 20, 20, 30, 40]
A tuple cannot be changed (no append)
List item at index 1: 20
A set has no index
Price of Bag: 600

"""

items_list = [10, 20, 20, 30]
items_tuple = (10, 20 ,20 ,30)
items_set = {10, 20, 20, 30}
items_dict = {"Pen":10, "Bag":600}

print("List: ", items_list, "length", len(items_list))
print("Tuple: ", items_tuple, "length", len(items_tuple))
print("Set: ", items_set, "length", len(items_set))
print("Dictionary: ", items_dict, "length", len(items_dict))

items_list.append(40)
print("List after append: ", items_list)

try:
    items_tuple.appent(40)
except AttributeError:
    print("A tuple cannot be changed (no append)")

print("List item at index 1: ", items_list[1])

try:
    items_tuple[1]
except TypeError:
    print("A set has no index")

print("Price of Bag: ", items_dict["Bag"])

"""
Two stores list the products they sell. Find the products that both stores sell. Each common product must appear only once in the result.

Example Input
store_a = ["Pen", "Notebook", "Bag", "Marker", "Pen"]
store_b = ["Marker", "Stapler", "Pen", "Ruler", "Bag"]

Expected Output
Common products: ['Pen', 'Bag', 'Marker']

"""

store_a = ["Pen", "Notebook", "Bag", "Marker", "Pen"]
store_b = ["Marker", "Stapler", "Pen", "Ruler", "Bag"]

common = []
for item in store_a:
    if item in store_b and item not in common:
        common.append(item)

print("Common products: ", common)

#Alternative method
common_1 = sorted(set(store_a) & set(store_b))
print("Common products:", common_1)

"""
Problem Statement
A list has order numbers. Split it into two lists: one with the even numbers and one with the odd numbers. Show both lists, their sizes and the sum of the even numbers.

Example Input
order_numbers = [12, 7, 24, 5, 18, 33, 40, 9]

Expected Output
Even numbers: [12, 24, 18, 40] (count: 4 )
Odd numbers: [7, 5, 33, 9] (count: 4 )
Sum of even numbers: 94

"""

order_numbers = [12, 7, 24, 5, 18, 33, 40, 9]

even = []
odd = []

for number in order_numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even Numbers: ", even, " (count: ", len(even), " )")
print("Odd Numbers: ", odd, " (count: ", len(odd), " )")
print("Sum of even numbers: ",sum(even))

# Alternative way
even = [number for number in order_numbers if number % 2 == 0]
odd = [number for number in order_numbers if number % 2 != 0]
print("Even Numbers: ", even, " (count: ", len(even), " )")
print("Odd Numbers: ", odd, " (count: ", len(odd), " )")
print("Sum of even numbers: ",sum(even))


"""
Problem Statement
Find the second-largest distinct value in a list of order amounts. The largest value may appear more than once, but the answer must be a different, smaller value.

Example Input
order_amounts = [4500, 6200, 6200, 3900, 5100]

Expected Output
Largest: 6200
Second largest: 5100

"""

order_amounts = [4500, 6200, 6200, 3900, 5100]

largest =  order_amounts[0]
for amount in order_amounts:
    if amount > largest:
        largest = amount

second_largest = None
for amount in order_amounts:
    if amount < largest:
        if second_largest is None or amount > second_largest:
            second_largest = amount    

print("Largest: ", largest)

print("Second largest: ", second_largest)

"""
Problem Statement
From a list of order amounts, extract the high-value orders (5000 or more). Do it with a loop and with a list comprehension. Then apply a 10% discount to the high-value orders and count how often 5500 appears.

Example Input
order_amounts = [1200, 5500, 800, 7200, 3000, 9100, 5500]

Expected Output
High orders (loop): [5500, 7200, 9100, 5500]
High orders (comprehension): [5500, 7200, 9100, 5500]
With 10% discount: [4950.0, 6480.0, 8190.0, 4950.0]
5500 appears 2 times

"""

order_amounts = [1200, 5500, 800, 7200, 3000, 9100, 5500]

high_order = []
for amount in order_amounts:
    if amount >= 5000:
        high_order.append(amount)

print("High orders (loop): ", high_order)

high_order_2 = [amount for amount in order_amounts if amount >= 5000]

print("High orders (comprehension): ", high_order_2)

discount = [round(amount * 0.9, 2) for amount in order_amounts]
print("with 10% discount: ", discount)

print("5500 appears ", order_amounts.count(5500), " times")

"""
Problem Statement
The number of orders for seven months is stored in a tuple. Find the lowest and highest values, how many months had 95 orders, which month number was the best, and the average.

Example Input
monthly_orders = (120, 95, 140, 95, 160, 110, 95)

Expected Output
Lowest: 95
Highest: 160
Months with 95 orders: 3
Best month number: 5
Average orders: 116.43

"""

monthly_orders = (120, 95, 140, 95, 160, 110, 95)

print("Lowest: ", min(monthly_orders))

print("Highest: ", max(monthly_orders))

print("Months with 95 orders: ", monthly_orders.count(95))

best_index = monthly_orders.index(max(monthly_orders))
print("Best month number: ", best_index + 1 )

avg_order = (sum(monthly_orders)/len(monthly_orders))
print("Average orders: ", round(avg_order,2))

"""
Problem Statement
Product names and prices are saved in two lists. Convert them to tuples, combine each name and price into a record, print the records, and then add a new product to the tuple (using a list in between).

Example Input
names = ["Pen", "Notebook", "Bag"]
prices = [10, 50, 600]

Expected Output
Names: ('Pen', 'Notebook', 'Bag')
Pen costs 10
Notebook costs 50
Bag costs 600
After adding Marker: ('Pen', 'Notebook', 'Bag', 'Marker')

"""

names = ["Pen", "Notebook", "Bag"]
prices = [10, 50, 600]

products_name = tuple(names) #create the name tuple
products_price = tuple(prices) #create the price tuple

print("Names: ", products_name)

products_record = [] #create the empty list to store append records

for index in range(len(products_name)):
    products_record.append((products_name[index], products_price[index])) #append name and price based upon the index

# print(products_record)

records = []
for index in range(len(products_name)):
    records.append((products_name[index], products_price[index]))

for product_name, product_price in products_record:
    print(product_name, " costs ", product_price)

temp_list = list(products_name)
temp_list.append("Marker")
new_tuple = tuple(temp_list)
print("After adding Marker: ", new_tuple)


"""
Problem Statement
A company has a set of customers who bought online and a set of customers who bought in a store. Find customers who used both channels, all customers, customers who used only online, and customers who used only the store.

Example Input
online = {"C101", "C102", "C103", "C104"}
store = {"C103", "C104", "C105"}

Expected Output
Used both channels: ['C103', 'C104']
All customers: ['C101', 'C102', 'C103', 'C104', 'C105']
Only online: ['C101', 'C102']
Only in store: ['C105']

"""

online = {"C101", "C102", "C103", "C104"}
store = {"C103", "C104", "C105"}

both = online.intersection(store) #intersection() keeps the values that are in both sets.
print("Used both channels:", sorted(both))

everyone = online.union(store) #union() combines all values from both sets, without repeats.
print("All customers:", sorted(everyone))

only_online = online.difference(store) #online.difference(store) keeps what is in online but not in store.
print("Only online:", sorted(only_online))

only_store = store.difference(online) #store.difference(online) is the opposite. It is a different result.
print("Only in store:", sorted(only_store))

"""
Problem Statement
Two warehouses hold different products. Find the products they both hold, the products that only one of them holds, the total number of different products, and check if both warehouses hold exactly the same products.

Example Input
warehouse_a = {"Pen", "Notebook", "Bag", "Marker"}
warehouse_b = {"Bag", "Marker", "Stapler", "Ruler"}

Expected Output
Common products: ['Bag', 'Marker']
Products in only one warehouse: ['Notebook', 'Pen', 'Ruler', 'Stapler']
Total different products: 6
Same products in both? False

"""

warehouse_a = {"Pen", "Notebook", "Bag", "Marker"}
warehouse_b = {"Bag", "Marker", "Stapler", "Ruler"}

common_product = warehouse_a.intersection(warehouse_b)
print("Common products: ", common_product)

only_one = warehouse_a.symmetric_difference(warehouse_b)
print("Products in only one warehouse: ", only_one)

total_products = warehouse_a.union(warehouse_b)
print("Total different products: ", total_products)

print("Same products in both? ", warehouse_a == warehouse_b)
