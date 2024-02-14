import datetime
now=datetime.datetime.now()
print("Current Date : ",end=" ")
print(now.strftime("%d-%m-%y"))
print("Current Time : ",end=" ")
print(now.strftime("%H:%M:%S"))


#Output:
# Current Date :  14-02-24
# Current Time :  21:42:58