total = 0
sandprice = 0
soadprice = 0
friedprice = 0
condomprice = 0
recipt = []
qty = 0

sand = input("What type of sandwich would you like? \nWe have Chicken for $5.25, Beef for $6.25, and Tofu for $5.75. ")

if sand == "Chicken" or sand == "chicken":
  total = 5.25
  sandprice = 5.25
if sand == "Beef" or sand == "beef":
  total = 6.25
  sandprice = 6.25
if sand == "Tofu" or sand == "tofu":
  total = 5.75
  sandprice = 5.75
recipt.append(sand)

recipt.append(sandprice)

beverage = input("Would you like a beverage? Yes or No. ")


if beverage == 'no' or beverage == 'No':
  beverage = ""
  size = ""
elif beverage == 'Yes' or beverage == 'yes':
  size = input("What size would you like? \nWe have Small for $1.00, Medium for $1.75, or large for $2.25. ")
  if size == "Small" or size == "small":
    soadprice = 1.00
    beverage == "Small"
  if size == "Medium" or size == "medium":
    soadprice = 1.75
    beverage == "Medium"
  if size == "Large" or size == "large":
    soadprice = 2.25
    beverage == "Large"
else:
  beverage = ""
  size = ""

if size != "":
  recipt.append(size)
  recipt.append(soadprice)

fried = input("Would you like fries with your meal? Yes or No. ")

if fried == "no" or fried == "No":
  fried = ""
  friedsize = ""
elif fried == "Yes" or fried == "yes":
  friedsize = input("What size? We have Small for $1.00, Medium for $1.50, or Large for $2.00 ")
  if friedsize == "Small" or friedsize == "small":
    megasize = input("Would you like to Megasize your fries? Yes or No. ")
    if megasize == "Yes" or megasize == "yes":
      friedprice == 2.00
    else:
      friedprice == 1.00
  elif friedsize == "Medium" or friedsize == "medium":
    friedprice = 1.50
  elif friedsize == "Large" or friedsize == "large":
    friedprice = 2.00
else:
  fried = ""
  friedsize = ""

if friedsize != "":
  recipt.append(friedsize)
  recipt.append(friedprice)

condommint = input("Would you like any Ketchup for $0.25 each? Yes or No. ")

if condommint == "No" or condommint == "no":
  condommint = ""

if condommint == "Yes" or condommint == "yes":
  qty = float(input("How many would you like? "))
  condomprice = qty * .25

if condommint != "":
  recipt.append(qty)
  recipt.append(condomprice)

total = friedprice + soadprice + sandprice + condomprice

print(sand, sandprice)
print(beverage, soadprice)
print(friedsize, friedprice)
print(qty, condomprice)
print(total)