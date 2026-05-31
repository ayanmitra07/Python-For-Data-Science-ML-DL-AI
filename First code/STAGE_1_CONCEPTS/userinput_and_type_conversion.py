#--------------------------------------
#SECTION 3: User Input and Type Conversion
#--------------------------------------
#Static software: in certain website the user gets the information and cannot provide any input.
# this is called static software. For example, a news website where users can only 
# read the news but cannot interact with it.

#dynamic software: in certain website the user can provide input and interact 
# with the website. For example, a social media website where users can post updates,
#  like and comment on posts, and interact with other users.
# To make a dynamic software it is mandatory to take user input and convert it
#  into the required data type.
# in python we can take user input using the input() function. 
# The input() function takes a string as an argument, 
# which is displayed to the user as a prompt. The function then waits 
# for the user to enter some input and returns it as a string.

#input()


name = input("Enter your name: ")
print("Hello", name)

first_num = input("Enter first number: ")
second_num = input("Enter second number: ")

# by default the input() function returns a string, so we need to convert it into an integer
first_num = int(first_num)
second_num = int(second_num)
sum = first_num + second_num
print("The sum of", first_num, "and", second_num, "is", sum)

#Type function and type conversion

#type function is used to check the data type of a variable or a value.
#  It returns the data type of the variable or value as a string.

inp_typ = type(4) #int
print(inp_typ)

inp_typ = type(4.5) #float
print(inp_typ)

inp_typ = type("Hello World") #str
print(inp_typ)

inp_typ = type(True) #bool
print(inp_typ)

inp_typ = type(1 + 2j) #complex
print(inp_typ)

inp_typ = type([1, 2, 3, 4, 5]) #list
print(inp_typ)

#Type conversion is the process of converting a value from one data type to another.
# we can use the built-in functions int(), float(), str(), bool() to convert a value 
# from one data type to another.

#implicit type conversion: in implicit type conversion, the python interpreter 
# automatically converts a value from one data type to another when it is necessary. 
# For example, when we add an integer and a float,
# the python interpreter automatically converts the integer to a float before performing the addition.

result = 4 + 4.5
print(result) #8.5

result = 4 + 4.5 + 1j
print(result) #(8.5+1j)

result = 4 + 4.5 + 1j + [1, 2, 3] # this will raise a TypeError because we cannot add a list to a number
print(result)

#explicit type conversion: in explicit type conversion, the programmer explicitly converts a value
# from one data type to another using the built-in functions int(), float(), str(), bool().

result = int(4.5) #4
print(result)

result = float(4) #4.0
print(result)

result = complex(4) #(4+0j)
print(result)

result = str(4) #"4"
print(result)  

result = bool(0) #False
print(result)

result = list("Hello World") #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
print(result)

result = tuple("Hello World") #('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(result)

result = set("Hello World") #{'H', 'e', 'l', 'o', ' ', 'W', 'r', 'd'}
print(result)

result = dict({"Name": "Ayan", "Age": 25, "City": "Pune"}) #{'Name': 'Ayan', 'Age': 25, 'City': 'Pune'}
print(result)

#type conversion is not a permanent change, it only changes the data type of the value for 
# that particular operation. 

#type casting is the process of converting a value from one data type to another using the built-in 
# functions int(), float(), str(), bool().
# type casting is a permanent change, it changes the data type of the value for all operations
