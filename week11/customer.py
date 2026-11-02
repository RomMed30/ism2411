#customers.py
#Author: Roman Medina
#Module 11 Lab: Customer Dictionary & Lookup

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
print(f"Discount Rate: {discount}")
