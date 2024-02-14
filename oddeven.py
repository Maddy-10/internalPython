nums=(1,2,3,4,5,6,7,8,9,)
cnt_odd=0
cnt_even=0
for i in nums:
    if not i%2:
        cnt_even+=1
    else:
        cnt_odd+=1
print("No.of Odd Nums : ",cnt_odd)
print("No.of Even Nums : ",cnt_even)


# Output:
# No.of Odd Nums :  5
# No.of Even Nums :  4