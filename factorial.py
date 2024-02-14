def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter The Number : "))
result = fact(n)
print("Factorial Of ",n," is : ",result)


#Output:
# Enter The Number : 5
# Factorial Of  5  is :  120