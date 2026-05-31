#-------------------------------
#SECTION 4: LITERALS
#-------------------------------

#Literals are the values that we use in our code. They can be of different data types such as
# integers, floats, strings, booleans, lists, tuples, sets, dictionaries, etc.
#It is a raw data given in a variable. There are different types of literals in python:
#1. String literals: A string literal is a sequence of characters enclosed in quotes.
#2. Integer literals: An integer literal is a whole number without a decimal point. 
#3. Float literals: A float literal is a number with a decimal point.
#4. Boolean literals: A boolean literal is a data type that can only have two values: True or False.
#5. List literals: A list literal is a collection of values enclosed in square brackets.
#6. Tuple literals: A tuple literal is a collection of values enclosed in parentheses.
#7. Set literals: A set literal is a collection of unique values enclosed in curly braces.
#8. Dictionary literals: A dictionary literal is a collection of key-value pairs enclosed in curly braces.

###############################################################################################

#Number literals can be of three types: integer literals, float literals and complex literals.

#Binary literals: A binary literal is a number represented in base 2. It is prefixed with "0b" or "0B". 
# For example, 0b1010 represents the binary number 1010, which is equal to 10 in decimal.

a = 0b1010

#Hexadecimal literals: A hexadecimal literal is a number represented in base 16. 
# It is prefixed with "0x" or "0X".

b = 0x12c

#Octal literals: An octal literal is a number represented in base 8. It is prefixed with "0o" or "0O".

c = 0o310

#Decimal literals: A decimal literal is a number represented in base 10. 
# It is the most common type of number literal and does not have any prefix.

d = 1234


#Float literals: A float literal is a number with a decimal point. 
# It can also be represented in scientific notation.

#for small numbers

float_1 = 10.5
print(float_1)

#for large numbers
# In scientific notation, the number is represented as a coefficient multiplied by 10 raised to a power.
# For example, 1.7e2 represents the number 1.7 multiplied by 10 raised to the power of 2.

float_2 = 1.7e2
print(float_2)

#for very small numbers
# In scientific notation, the number is represented as a coefficient multiplied by 10 raised to a negative power.
# For example, 1.7e-2 represents the number 1.7 multiplied by 10 raised to the power of -2.

float_3 = 1.7e-2
print(float_3)

#Complex literals: A complex literal is a number that has a real part and an imaginary part.
# In Python, the imaginary part is represented by the letter "j" or "J".
#it can be represented in the form of a + bj, where a is the real part and b is the imaginary part.
#it can also be written without the real part, in which case it is assumed to be 0. 
# For example, 3j represents the complex number 0 + 3j.

x = 2 + 3j
print(x)

print(x,x.real,x.imag)

#####################################################################################################

#String literals: A string literal is a sequence of characters enclosed in quotes.
# In Python, you can use single quotes (' '), double quotes (" ") or triple quotes (''' ''' or """ """)
#  to create a string literal.

string_1 = 'Hello World'

string_2 = "Hello World"

string_3 = "C"

multiline_string = """This is a multiline string. It can span multiple lines."""

unicode_string = u"\U0001F600\U0001F606\U0001F923" 

raw_string = r"raw \n string"

print(string_1)
print(string_2)
print(string_3)
print(multiline_string)
print(unicode_string)
print(raw_string)

#############################################################################################

#Boolean literals: A boolean literal is a data type that can only have two values: True or False.
#we can also use boolean literals as integer literals, where True is represented as 1 and 
# False is represented as 0.

a = True + 4

b = False + 10

print("a =", a) #5 
print("b =", b) #10

#################################################################################################


#Special literals: Python has three special literals: None, Ellipsis and NotImplemented.

#None is a special literal that represents the absence of a value or a null value.
# It is often used to indicate that a variable has no value or that a function does not return anything.

#reason for using None:

#1. To indicate that a variable has no value: When you want to create a variable
# that does not have a value, you can assign it the value None. 
# This is useful when you want to initialize a variable but do not have a value to assign to it yet.

#2. To indicate that a function does not return anything: When you want to create a function
# that does not return anything, you can use the return statement without any value or with the value None.
# This is useful when you want to create a function that performs an action but does not need to return any value.
# so a= 0 is not the same as a = None, because a = 0 is an integer literal and a = None is a special 
# literal that represents the absence of a value.

a = None
print(a)

