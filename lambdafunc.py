x=int(input("Enter X Value :"))
y=int(input("Enter Y Value :"))
a=lambda x,y:x+y
print("Add : ",a(x,y))
b=lambda x,y:x-y
print("Sub : ",b(x,y))
c=lambda x,y:x*y
print("Mul : ",c(x,y))
d=lambda x,y:x/y
print("Div : ",d(x,y))
e=lambda x,y:x%y
print("Mod : ",e(x,y))


#Output :
# Enter X Value :10
# Enter Y Value :5
# Add :  15
# Sub :  5
# Mul :  50
# Div :  2.0
# Mod :  0