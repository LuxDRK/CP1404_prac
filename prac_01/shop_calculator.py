num = int(input("Number of items: "))
while num < 0:
    print("Invalid number of items!")
    num = num = int(input("Number of items: "))
price = 0
for i in range(0,num):
    price = price + float(input("Price of item: "))
if price > 100:
    print("Total price for ",num," items is $",round(price*0.9,2))
else:
    print("Total price for ", num, " items is $",round(price,2))