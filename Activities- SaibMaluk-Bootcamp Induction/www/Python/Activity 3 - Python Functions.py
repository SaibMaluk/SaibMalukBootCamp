

num = 8
# If  number is greater than 1
if num > 1:
    # Iterate
    for i in range(2, (num//2)+1):

        
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
