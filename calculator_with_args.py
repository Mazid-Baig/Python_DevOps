# //* Function --
# 1.takes the input
# 2.performs the required logic
# 3.returns the output
import sys
# sys module is used for reading cli arguements

def addition(num1, num2):
    total = num1 + num2
    return total

def substraction(num1, num2):
    total = num1 - num2
    return total

num1 = float(sys.argv[1])
# by default cli arguements are read as strings there fore we typecast to float
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = addition(num1, num2)
    print(output)

if operation == "sub":
    output = substraction(num1, num2)
    print(output)







