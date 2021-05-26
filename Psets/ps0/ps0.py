"""
1. Asks the user to enter a number “x” 
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”. 
4. Prints out the log (base 2) of “x”.
"""
import math

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
print("x**y = " , x**y)
print("log(x) =  " , math.log2(x))