#Self Assessment Questions
#1. The first bug I spotted was the one with the indexes. I used the trace back to find it while I was scanning the code for error. I think I know the basics on debugging
#2. `apply_discount` takes a `price` (a number) and a `tier` (a string like `"gold"`, `"silver"`, or `"bronze"`) and returns the price after taking off 15%, 10%, 5%, or nothing for any other tier. A colleague could guess the basic idea from the name, but they couldn't use it reliably because nothing tells them the tier names or that a misspelled tier silently gets no discount.
#3. I used ai when I was debugging my exercise 5 because I could not figure the last bug. I pasted in the error messsage and was able to figure what was going wrong so therefore I do believe it helped my understanding.


# --Exercise 1 --

# define a function to calculate tax

def calculate_tax(price, rate):
    return price * rate

# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7% is: ${tax1:.2f}")
print(f"Tax for $250 at 8% is: ${tax2:.2f}")
print(f"Tax for $350 at 5% is: ${calculate_tax(350, 0.05):.2f}")

#--Exercise 2--

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else: 
        return price

# calling the function with different tiers
original_price = 200

for tier in ["gold" , "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#conditionals are inside the function, the function is inside the loop

#--Exercise 3 --

def final_price(price, discount_tier, tax_rate):
    discounted = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

#-- Calling the final_price function
print(f"final_price(200,'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")
# --Exercise 4--

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none"  )]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Total: {total:.2f}")

#exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale #change == to += so it overwrites total on every pass instead of adding to it
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    #change operator from <= because there is only 5 indexes, 0;1;2;3;4, 
    print(sales[i])
    i += 1


# --Exercise 6--

x = 10  # global variable

def double_it():
    x = 999        # local variable, separate from the global x
    return x * 2

print(x)            # 10
print(double_it())  # 1998
print(x)            # still 10, because the function didn't change the global x

