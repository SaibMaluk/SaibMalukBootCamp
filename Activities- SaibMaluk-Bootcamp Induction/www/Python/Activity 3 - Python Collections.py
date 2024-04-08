#Activity 3 - Python Collections



myList= [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

themax = myList[0] # starting with the first value as max
theMin =myList[0] # starting with it as min to compare
for num in myList:
    if num > themax:
        themax = num
    if num < theMin:
        theMin = num

print("Maximum value for the above list = ", themax) 
print("Minimum value for the above list = ", theMin) 
