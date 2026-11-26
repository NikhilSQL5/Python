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
