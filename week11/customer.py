#customers.py
#Author: Roman Medina
#Module 11 Lab: Customer Dictionary & Lookup

# 1. I'd use bracket notation (d["key"]) when the key must exist, like a
#    required field such as a customer ID, because a KeyError flags bad data
#    right away. I'd use .get("key", default) when a key is optional or might
#    be missing, like a discount code. Rule of thumb: brackets for required
#    data, .get() for optional data with a sensible default.
#
# 2. Building a summary dictionary is like a SUMIF or a PivotTable in Excel:
#    group rows by a category and total a value column. Python scales better
#    for large datasets because it handles millions of rows without slowing
#    down or hitting row limits, and the script can be rerun on new data
#    automatically instead of rebuilding formulas by hand.



print("--Exercise 1--")
customers = {
    "name": "Alice", # Key: Value , 
    "email": "alice@example.com",
    "tier": "Gold", 
    "ytd_spend": 12400,
}

print(customers["name"])
print(customers["email"])
print(customers["tier"])
print(customers["ytd_spend"])

print("--Exercise 2--")
customers["phone"] = "555-1234" #adding a new key-value pair to the dictionary
print(customers)
customers["tier"] = "platinum"
print(customers)
del customers ["name"]
print(customers)

print(customers.get("name", "not found"))
print(customers.get("email", "not found"))
print(customers.get("tier", "not found"))
print(customers.get("ytd_spend", 0))



print("--Exercise 3--")
print(customers.get("email", "no email on file"))

# try:
#     print(customers["email"])
# except KeyError:
#     print("KeyError caught: " "no email on file")

print("--Exercise 4--")

for key, value in customers.items():
    print(f"{key}: {value}")

for something in customers:
    print(something, customers[something])

print("--Exercise 5--")
tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.1,
                  "platinum": 0.15}

purchase = 200
discount = tier_discounts.get(customers.get("tier", 0), 0)
final_price = purchase * (1 - discount)
print(f"Tier: {customers["tier"]}")
print(f"Discount Rate: {discount * 100}%")
print(f"Final Price: {final_price}")

tier_discounts = {"Bronze": 0.05, "Silver": 0.10, "Gold": 0.15}

 
print("--Exercise 6--")
customers = [
    {"name": "Alice", "tier": "Gold"},
    {"name": "Ben", "tier": "Silver"},
    {"name": "Carla", "tier": "Bronze"},
]
 
purchase = 300
for customer in customers:
    rate = tier_discounts.get(customer["tier"], 0)
    discount = purchase * rate
    print(f"{customer['name']} ({customer['tier']}): ${discount:.2f} off a ${purchase} purchase")
 
print("--Exercise 7--")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
 
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} units left")
 

print("--Exercise 8--")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
 
summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]
 
for region in sorted(summary):
    print(f"{region}: {summary[region]}")