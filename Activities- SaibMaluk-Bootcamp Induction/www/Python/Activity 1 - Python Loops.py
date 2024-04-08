# Activity 1 - Python Loops


x,y=0, 1

# Execute the while loop until the value of 'y' becomes greater than or equal to 50
while y < 50:
    # Print the current value of 'y'
    print(y)
    
    # Update the values of 'x' and 'y'
    #  'x' becomes the previous value of 'y'
    #  'y' becomes the sum of 'x' 
    x, y = y, x + y


