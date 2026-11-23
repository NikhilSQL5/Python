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
