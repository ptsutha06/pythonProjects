
import math as ma

#math is module of python
#Math Operators
a = 5
b = 6
print(a+b) #Addition
print(a-b) #Substraction
print(a*b) #Multipilication
print(a/b) #Division
c = 7.86
print(round(c)) #Round off
d = -5
print(abs(d)) #Absolute Value
print(pow(a,3)) #Power of
print(a**5) #Power of
print(max(a,b))
print(min(a,b))

#functions in math module
a = 4.56
print(ma.ceil(a))
print(ma.floor(a))
print(ma.factorial(5))

#Assignment
#Get user input - Get a number n from user. Compute and Print the following values.
'''
1. log2(n)
2. Cos(n)
3. e^n
'''

n = int(input("Enter a number:"))
print("1. Log base 2 value is: " + str(ma.log2(n)))
print("2. Cosine value is: " + str(ma.cos(n)))
print("3. e to the power value is: " + str(ma.exp(n)))

#Relational Operators
num = 20
print(num > 20) #Greater than
print(num < 20) #Less than
print(num >= 20) #Greater than or equal to
print(num <= 20) #Less than or Equal to
print(num == 25) #Equal to
print(num != 25) #Not equal to
