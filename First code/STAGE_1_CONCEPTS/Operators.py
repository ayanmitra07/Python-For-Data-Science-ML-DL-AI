#---------------------------------------------------------
#SECTION 5: Operators
#---------------------------------------------------------

#Operators are special symbols that perform specific operations on one or more operands.
#It is used to perform operations on variables and values. The value that the operator 
# operates on is called an operand.
#Python has several types of operators, including:
#Arithmetic operators: +, -, *, /, %, **, //
#Comparison operators: ==, !=, >, <, >=, <=
#Logical operators: and, or, not
#Assignment operators: =, +=, -=, *=, /=, %=, **=, //=
#Bitwise operators: &, |, ^, ~, <<, >>
#Membership operators: in, not in
#Identity operators: is, is not
#Operator precedence: in python, operators have a precedence order, which determines the order in which
# operations are performed in an expression. The operator precedence can be changed using parentheses ().

#########################################################################################################

#Arithmetic operators: Arithmetic operators are used to perform mathematical operations on numbers.

a = 10
b = 3

print("a + b =", a + b) #Addition: 13
print("a - b =", a - b) #Subtraction: 7
print("a * b =", a * b) #Multiplication: 30
print("a / b =", a / b) #Division: 3.3333333333333335
print("a % b =", a % b) #Modulus: 1
print("a ** b =", a ** b) #Exponentiation: 1000
print("a // b =", a // b) #Floor division: 3
print("a + b * 2 =", a + b * 2) #Operator precedence: 16
print("(a + b) * 2 =", (a + b) * 2) #Operator precedence with parentheses: 26

###########################################################################################################

#Comparison operators: Comparison operators are used to compare two values and return 
# a boolean value (True or False) based on the comparison.

a = 10
b = 28

print("a == b:", a == b) #Equal to: False
print("a != b:", a != b) #Not equal to: True
print("a > b:", a > b) #Greater than: False
print("a < b:", a < b) #Less than: True
print("a >= b:", a >= b) #Greater than or equal to: False
print("a <= b:", a <= b) #Less than or equal to: True
print("a == 10:", a == 10) #Equal to: True
print("b != 28:", b != 28) #Not equal to: False

#############################################################################################################

#Logical operators: Logical operators are used to combine multiple boolean expressions and return 
# a boolean value based on the combination.

a = True
b = False

print("a and b:", a and b) #Logical AND: False
print("a or b:", a or b) #Logical OR: True
print("not a:", not a)  #Logical NOT: False, The not operator negates the value of a, so if a is True,
                        #not a will be False, and if a is False, not a will be True.

print("not b:", not b) #Logical NOT: True

#############################################################################################################

#Bitwise operators: Bitwise operators are used to perform bitwise operations on integers.
# A usecase of bitwise operator will be when we image process, we can use bitwise operators 
# to manipulate the pixels of the image by putting filters. 


a = 5 # in binary: 0101
b = 3 # in binary: 0011

print("a & b:", a & b)  #Bitwise AND: 1 (in binary: 0001). This & OPERATOR is not the same as the and operator,
                        #the & operator performs a bitwise AND operation on the binary representation of the operands,
                        #while the and operator performs a logical AND operation on the boolean values of the operands.

print("a | b:", a | b) #Bitwise OR: 7 (in binary: 0111). The | operator performs a bitwise OR operation on the binary 
                        #representation of the operands, while the or operator performs
                        #a logical OR operation on the boolean values of the operands.

print("a ^ b:", a ^ b)  #Bitwise XOR: 6 (in binary: 0110). The ^ operator performs a bitwise XOR operation 
                        #on the binary representation of the operands, while the xor operator is not 
                        #a built-in operator in Python, but it can be implemented using the ^ operator.

print("~a:", ~a) #Bitwise NOT: -6 (in binary: 1010)
print("a << 1:", a << 1) #Bitwise left shift: 10 (in binary: 1010)
print("a >> 1:", a >> 1) #Bitwise right shift: 2 (in binary: 0010)

######################################################################################################

#Assignment operators: Assignment operators are used to assign values to variables. 
# They can also be used to perform an operation and assign the result to a variable in a single step.

i = 2
i += 3 #i = i + 3
print("i += 3:", i) #i = 8

i -= 2 #i = i - 2
print("i -= 2:", i) #i = 6

i *= 4 #i = i * 4
print("i *= 4:", i) #i = 24

i /= 6 #i = i / 6
print("i /= 6:", i) #i = 4.0

g = 7
g %= 3 #g = g % 3
print("g %= 3:", g) #g = 1

h = 5
h **= 2 #h = h ** 2
print("h **= 2:", h) #h = 25

h //= 2 #h = h // 2
print("h //= 2:", h) #h = 12

######################################################################################################

#Identity operators: Identity operators are used to compare the memory locations of two objects.
# The is operator returns True if both operands refer to the same object in memory, and False
# otherwise. The is not operator returns True if both operands do not refer to the same object in memory,
# and False otherwise.  

a = [1, 2, 3]
b = [1, 2, 3]

print("a is b:", a is b) #False, because a and b are two different objects in memory, 
                            #even though they have the same values.

a = 24
b = 24
print("a is b:", a is b) #True, because small integers are cached by Python and refer to the same object in memory.

a = "Hello-World"
b = "Hello-World"
print("a is b:", a is b) #False, because string literals that are not identifiers are not interned by Python and refer to different objects in memory.

a = 1 + 2j
b = 1 + 2j
print("a is b:", a is b) #False, because complex numbers are not cached by Python and refer to different objects in memory.

########################################################################################################

#membership operators: Membership operators are used to test whether a value is present 
# in a sequence (such as a list, tuple, or string) or not. The in operator returns True if 
# the value is present in the sequence, and False otherwise. The not in operator returns True 
#if the value is not present in the sequence, and False otherwise.

x = "K"
print("x in 'Kolkata':", x in "Kolkata")  #True
print("x not in 'Kolkata':", x not in "Kolkata")  #False


x = [1, 2, 3]
print("5 in x:", 5 in x)  #False

y  = (4, 5, 6)
print("5 in y:", 5 in y) #True

z = {"Name": "Ayan", "Age": 25, "City": "Pune"}
print("25 in z:", 25 in z) #False, because the in operator checks for the presence of 
                         #the value in the keys of the dictionary, not the values.

d = {"Name": "Ayan", "Age": 25, "City": "Pune"}

 