# Activity 2 - Python Functions
# factorial of number 6 
def myFactorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

# example number 6
myNum = 6
print("The factorial of ",myNum,"is", myFactorial(myNum))
