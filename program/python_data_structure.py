"""
Problem Statement
A shop saves its daily sales for one week in a list. Show the first day, the last day, the first three days, the last two days, the number of days, and every second day.

Example Input
daily_sales = [1200, 3400, 2800, 4500, 3900, 1500, 4100]

Expected Output
First day: 1200
Last day: 4100
First three days: [1200, 3400, 2800]
Last two days: [1500, 4100]
Number of days: 7
Every second day: [1200, 2800, 3900, 4100]

"""

# solution

daily_sales = [1200, 3400, 2800, 4500, 3900, 1500, 4100]

print(f"First day: {daily_sales[0]}")
print(f"Last day: {daily_sales[-1]}")
print(f"First three days: {daily_sales[0:3]}")
print(f"Last two days: {daily_sales[-2:]}")
print(f"Number of days: {len(daily_sales)}")
print(f"Every second day: {daily_sales[::2]}")

"""

Problem Statement
An order record has an order ID, a customer name and an amount. Pack the values into a tuple, then unpack them into separate variables. Also swap two variables.

Example Input
order values: "ORD-101", "Asha", 2400
low = 500
high = 100

Expected Output
Packed tuple: ('ORD-101', 'Asha', 2400)
Order ID: ORD-101
Customer: Asha
Amount: 2400
After swap: low = 100 , high = 500


"""

order_values = ["ORD-101", "Asha", 2400]  #packing

print("Packed tuple: ", order_values)

order_id,customer,amount = order_values  #un-packing

print("Order ID: ",order_id)
print("Customer: ",customer)
print("Amount: ",amount)

low = 500
high = 100

low, high = high, low  #swap

print("Afrer swap: low = ", low, "high = ", high)

"""

Problem Statement
A product record is saved as a tuple (name, price, category, units in stock). Read parts of the record, and show that a tuple cannot be changed.

Example Input
product = ("Laptop", 45000, "Electronics", 12)

Expected Output
Name: Laptop
Price: 45000
Last item: 12
First two items: ('Laptop', 45000)
Number of items: 4
A tuple cannot be changed

"""

product = ("Laptop", 45000, "Electronics", 12)

print("Name: ",product[0])
print("Price:", product[1])
print("Last item: ",product[-1])
print("First two items: ",product[:2])
print("Number of items: ", len(product))

try:
    product[1] = 40000
except TypeError:
    print("A tuple cannot be changed")

"""

Problem Statement
A list has order amounts. Sort them, reverse them, count how often an amount appears, find the position of the largest amount, and check if an amount exists.

Example Input
order_amounts = [2500, 800, 12000, 450, 9500, 800]

Expected Output
Original: [2500, 800, 12000, 450, 9500, 800]
Sorted copy: [450, 800, 800, 2500, 9500, 12000]
Original is unchanged: [2500, 800, 12000, 450, 9500, 800]
After sort(): [450, 800, 800, 2500, 9500, 12000]
After reverse(): [12000, 9500, 2500, 800, 800, 450]
800 appears 2 times
Position of 12000: 0
Is 450 in the list? True

"""

order_amounts = [2500, 800, 12000, 450, 9500, 800]

print("Original: ", order_amounts)
print("Sorted copy: ",sorted(order_amounts))
print("Original is unchanged: ", order_amounts)

order_amounts.sort()
print("After sort(): ", order_amounts)

order_amounts.reverse()
print("After reverse(): ", order_amounts)

print("800 appears ", order_amounts.count(800), "times")
print("Position of 12000: ", order_amounts.index(12000))

print("Is 450 in the list? ", 450 in order_amounts)

"""

Problem Statement
A stationery shop manages its product list. Add, change and remove products using list methods, and show the list after each step.

Example Input
products = ["Pen", "Notebook", "Bag"]

Expected Output
Append: ['Pen', 'Notebook', 'Bag', 'Marker']
Insert: ['Pen', 'Stapler', 'Notebook', 'Bag', 'Marker']
Extend: ['Pen', 'Stapler', 'Notebook', 'Bag', 'Marker', 'Ruler', 'Eraser']
Update: ['Gel Pen', 'Stapler', 'Notebook', 'Bag', 'Marker', 'Ruler', 'Eraser']
Remove: ['Gel Pen', 'Stapler', 'Notebook', 'Marker', 'Ruler', 'Eraser']
Popped item: Eraser
Final list: ['Gel Pen', 'Stapler', 'Notebook', 'Marker', 'Ruler']

"""

products = ["Pen", "Notebook", "Bag"]

products.append("Marker")
print("Append: ",products)

products.insert(1,"Stapler")
print("insert: ", products)

products.extend(["Ruler","Eraser"])
print("Extend: ",products)

products[0] = "Gel Pen"
print("Update: ",products)

products.remove("Bag")
print("Remove: ", products)

remove_item = products.pop()
print("Popped item: ", remove_item)

print("Final list: ", products)

"""

Problem Statement
A business has its monthly sales for six months in a list. Find the highest month, the lowest month, the total sales and the average monthly sales (rounded to 2 decimals).

Example Input
monthly_sales = [45000, 52000, 38000, 61000, 49000, 57000]

Expected Output
Highest month: 61000
Lowest month: 38000
Total sales: 302000
Average sales: 50333.33

"""

monthly_sales = [45000, 52000, 38000, 61000, 49000, 57000]

highest = max(monthly_sales)
lowest = min(monthly_sales)
total = sum(monthly_sales)
avg_sales = round(total/len(monthly_sales),2)

print("Highest month: ",highest)
print("Lowest month: ", lowest)
print("Total sales: ", total)
print("Average sales: ", avg_sales)

"""
Problem Statement
A list of customer IDs has repeated entries. Find the unique customers and count them.

Example Input
customer_ids = [101, 102, 103, 102, 104, 101, 105]

Expected Output
Unique IDs: [101, 102, 103, 104, 105]
Total entries: 7
Unique customers: 5
Is 104 a customer? True

"""

customer_ids = [101, 102, 103, 102, 104, 101, 105]

unique_ids = set(customer_ids)

print("Unique IDs: ", unique_ids)
print("Total entries: ", len(customer_ids))
print("Unique customers: ", len(unique_ids))
print("Is 104 a customer? ", 104 in customer_ids)

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

