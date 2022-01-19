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
