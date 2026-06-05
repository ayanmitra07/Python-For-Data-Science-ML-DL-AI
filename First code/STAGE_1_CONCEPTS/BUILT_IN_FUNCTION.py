#---------------------------------------------------------------
#SECTION 12: BUILT IN FUNCTIONS
#---------------------------------------------------------------

#BUILT IN FUNCTIONS: Python provides a wide range of built-in functions that are readily available for use.
# These functions perform various tasks, such as mathematical operations, string manipulation,
# and data type conversions. Some commonly used built-in functions include:

#1. print(): This function is used to display output on the console. It can take multiple arguments and
#   can be used to format the output in various ways.

first_name = "James"
last_name = "Bond"
print("Hello, " + first_name + " " + last_name + "!")  # Output: Hello, James Bond!

#2. Input(): This function is used to take input from the user. 
# It reads a line of text from the console and returns it as a string.
user_input = input("Enter your name: ")
print("Hello, " + user_input + "!")

#3. len(): This function is used to get the length of a string, list, tuple, or any other iterable.

len("Kolkata")  # Output: 8

len([2,8,3,5,1,2])  # Output: 6

len((1, 2, 3, 4, 5, 2, 1))  # Output: 5

#4. type(): This function is used to get the data type of a variable or value in Python. 
# It returns the type of the object passed as an argument.

a = 10.2
b = "Hello"
type(a)  # Output: <class 'float'>
print(type(b))  # Output: <class 'str'>

#5. Type Conversion Functions: int(), float(), str(): These functions are used to convert values from 
# one data type to another.

ty = int("100")
print(type(ty))

#6. range(): This function is used to generate a sequence of numbers. It can take one, two, or three arguments
#   to specify the start, stop, and step values for the sequence.

list(range(5))  # Output: [0, 1, 2, 3, 4]

#7  . sum(): This function is used to calculate the sum of a list of numbers.

sum([4, 6, 2, 5])  # Output: 17, the sum of the numbers in the list

sum((1, 2, 3, 4, 5))  # Output: 15, the sum of the numbers in the tuple

sum({5,4, 22}) # Output: 31, the sum of the numbers in the set

#8. abs(): This function is used to get the absolute value of a number. this is just 
# like a modulus operator in other programming languages.

abs(-27)  # Output: 27

#9. pow(): This function is used to calculate the power of a number. 
# It takes two arguments: the base and the exponent.

pow(2,-4)

pow(3, 8)  # Output: 6561

#10. max() and min(): These functions are used to find the maximum and minimum values from a list of numbers.
#here we first pass an itearable to the min/max function and then we can also 
# pass multiple arguments to the min/max function to find the minimum/maximum value among them.

min([5, 2, 9, 1])  # Output: 1

max(5, 2, 9, 1)  # Output: 9

max("Kolkata") # Output: 't' (the maximum character based on ASCII values)

#11. round(): This function is used to round a floating-point number to a 
# specified number of decimal places.

c = 22/7
print(c)  # Output: 3.142857142857143

round(c,4)  # Output: 3.1429

#12. divmod(): This function is used to perform integer division and modulus operations simultaneously.
# It takes two arguments and returns a tuple containing the quotient and the remainder.

divmod(13,5)  # Output: (2, 3) (2 is the quotient and 3 is the remainder)

#13. id(): This function is used to get the unique identifier of an object in Python.

x = 27

id(x)  # Output: (a unique identifier for the variable x)

