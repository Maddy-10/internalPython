l=[]
n=int(input("Enter The No.of. Elements : "))
print("Enter The Values in the List : ")
for i in range(n):
    a=int(input(" "))
    l.append(a)
    temp=l[0]
for j in range (n):
    if(temp<l[j]):
        temp=l[j]
print("The Largest Value in the List : ",temp)

# Output :
# Enter The No.of. Elements : 4
# Enter The Values in the List : 
#  10
#  15
#  103
#  6
# The Largest Value in the List :  103