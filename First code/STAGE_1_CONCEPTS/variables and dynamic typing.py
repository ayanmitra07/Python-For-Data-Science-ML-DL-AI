#--------------------------------------
#SECTION 2: Variables, Dynamic Typing and Data Types(- Integer, - String, - Float, - Boolean)
#--------------------------------------

#Variables
# A variable is a container for storing data values. In Python, you can create a 
# variable and assign a value to it using the assignment operator (=).
# The name of the variable is called an identifier, and it must follow certain rules.

#Dynamic Typing
# Python is a dynamically typed language, which means that you do not need to declare the type of 
# a variable when you create it. The type of a variable is determined at runtime based on the 
# value assigned to it. This allows for greater flexibility in programming, as you can change the 
# type of a variable simply by assigning a new value to it.

#Data Types
# Python has several built-in data types that are used to represent different types of data. 
#String(str): A string is a sequence of characters enclosed in quotes.
#Integer(int): An integer is a whole number without a decimal point.
#Float(float): A float is a number with a decimal point.
#Boolean(bool): A boolean is a data type that can only have two values: True or False.

#dynamic typing
x = 5
print(x)
x = "Hello World"
print(x)
x = 3.14
print(x)
x = True
print(x)

#special syntax
a = 5; b = 10; c = 15
print(a)
print(b)
print(c)

a, b, c = 5, 24 , 17
print(a)
print(b)
print(c)

a = b = c = 5
print(a)
print(b)
print(c)
