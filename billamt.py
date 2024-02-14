product = input("Enter Product Name : ")
amt = int(input("Enter Product Price : "))
qty = int(input("Enter Product Quantity : "))
dis = int(input("Enter Product Discount in % : "))
tax = int(input("Enter Tax Amount in % : "))
tot = amt*qty
tax = tax/100
dis = dis/100
dis_amt = tot * dis
tax=amt*tax
billamt = tot-dis_amt+tax


print("Product : ",product)
print("Price : ",tot)
print("Quantity : ",qty)
print("Discount : ",dis_amt)
print("Bill Total : ",billamt)

# Output :
# Enter Product Name : Paste
# Enter Product Price : 40
# Enter Product Quantity : 2
# Enter Product Discount in % : 10
# Enter Tax Amount in % : 18
# Product :  Paste
# Price :  80
# Quantity :  2
# Discount :  8.0
# Bill Total :  86.4.

