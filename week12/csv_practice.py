# csv_practice.py
#Author: Roman Medina
#Module 12 Lab: Read a Sales CSV, Write a Cleaned up report

import csv
from datetime import datetime
from itertools import product

SALES_FILE = "week12/data/sales.csv"
CLEANED_FILE = "week12/cleaned_sales.csv"
LOG_FILE = "week12/run_log.txt"

print("--Exercise 1--")
with open(SALES_FILE, "r") as f:
    print(f"Opened {SALES_FILE}.")

print("--Exercise 2--")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("--Exercise 3--")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)   # read the first row (column names) and move past it
    print("Header:", header)
    for row in reader:
        print(row)


print("--Exercise 4--")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")


print("--Exercise 5--")
rows_read = 0
high_value = []
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader) 
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Quantity", "Total"])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")

print("--Exercise 6--")

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ")

print("--Exercise 7--")
summary = {}    
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("--Exercise 8--")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:   # "a" = append, keeps earlier lines
    f.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")
print(f"Logged run to {LOG_FILE}.")

# Reflection 1: Doing this in Excel means opening the file, adding a Total
# column, filtering, and saving by hand, which is quick for a one-time job.
# Python can repeat the whole pipeline in one run on any number of files and
# never makes a copy-paste mistake. Excel is still easier for quickly looking
# at data, making charts, and sharing with people who don't code.
#
# Reflection 2: A restaurant could log each night's closing sales total to a
# file so managers can track revenue day by day. Append mode is the right tool
# because each run adds a new line instead of overwriting the earlier nights,
# so the full history builds up automatically.


    
