
#inventory.py
# Author: Roman Medina
#
# Reflection 1: The most surprising thing was that list indexing starts at 0, and that negative indexes let you count backward from the end without knowing the list’s length. I also didn’t expect methods like .sort() and .remove() to change the original list in place instead of making a new copy, which is different from how tuples work.
#
# Reflection 2: In my hospitality class we discussed how restaurant managers track inventory and daily sales. Instead of manually filtering rows in Excel to find which days sales went above a target, a Python list and a simple loop could pull out those days, count them, and average them instantly. It would also be reusable every week without redoing the same clicks.

#Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Exercise 2
print("---Exercise 2: Index Practice---")
print(inventory[0]) # always grabs the first item
print(inventory[-1]) # always grabs the last item

middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item (not hard coded)

#Exercise 3
print("---Exercise 3: Slicing Practice---")
print(inventory[:3]) # grabs the first three items (index 0 to 2)
print(inventory[-2:]) # grabs the last two items
print(inventory[::2]) # grabs every other item, starting at index 0

print("---Exercise 4: List Methods---")
inventory.append("envelope") # adds item to the end of the list
print(inventory)
inventory.remove("tape") # removes item from the list
print(inventory)
inventory.sort() # sorts the list in alphabetical order
print(inventory)

print("---Exercise 5: Tuple comparison---")
coords = (40.7128, -74.0060) # creates a tuple with two values
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")
print(coords) # original coords are unchanged

print("---Exercise 6: Average of a list of sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"The total sales is: {total}")
print(f"The number of sales is: {count}")
print(f"The average sales is: {average}")
print(f"The best sale is: {max(sales)}")
print(f"The worst sale is: {min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"The best sale is: {best}")
print(f"The worst sale is: {worst}")

print("---Exercise 7: Accumulator pattern---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2)) # applies a 10% discount and rounds to 2 decimal places
print(prices)
print(discounted)

print("---Exercise 8: Filter above threshold---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")