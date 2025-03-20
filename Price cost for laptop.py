import os
os.system('cls')
customer = input ("enter customer name:")
Product = input("Enter product name:")
Qty = int(input("enter Quanity:"))
price = float(input("enter price:"))
total = Qty*price
print(f"{customer}ordered (product)and it's the total price is ${total}")
print("jason ordered laptop and it's total price is $2000.00")

#jason ordered LAtop and it's total price is $2000.00
#ask user if user wants to continue
cont = input("Would you like to continue? (y/n):")
if cont =='y' or cont == 'y':
    customer_1 = input('enter customer name:')
    product_1= int(input("enter Quanity:"))
    price_1 = float(input("enter price:"))
    total_1 = Qty*price
    print(f"{customer_1} Ordered {product_1} and it's total price is ${total_1}")