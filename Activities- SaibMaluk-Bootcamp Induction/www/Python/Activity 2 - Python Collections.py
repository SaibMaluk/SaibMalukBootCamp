#Activity 2 - Python Collections


# Driver Code
lst = [20, 30, 25, 35, -16, 60, -100]
sum_of_list = 0
for i in range(len(lst)):
        sum_of_list += lst[i]
        average = sum_of_list/len(lst)

print("Average value of the list elements is : ", round(average, 1))
