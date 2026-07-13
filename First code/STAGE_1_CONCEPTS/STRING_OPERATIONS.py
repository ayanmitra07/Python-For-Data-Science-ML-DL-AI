#----------------------------------------------------------------------
#SECTION 14: STRINGS IN PYTHON : STRING OPERATIONS (PART 4)
#----------------------------------------------------------------------

# ARITHMETIC OPERATIONS ON STRINGS

# Unlike numbers, strings support only a limited set of arithmetic
# operations in Python.

# The two arithmetic operators commonly used with strings are:
# 1. +  (Concatenation)
# 2. *  (Repetition / String Multiplication)

# 1. STRING CONCATENATION (+)
# The '+' operator joins two or more strings together.
# This process is called CONCATENATION.

first_string = "Hello "
second_string = "AYAN!"

print(first_string + second_string) # Output: Hello AYAN!

# Important:
# Both operands must be strings. Example:
# print("Hello" + 10)
# ERROR: TypeError: can only concatenate str (not "int") to str

#2. STRING MULTIPLICATION (*)
# The '*' operator repeats a string a specified number of times.

print("Hi " * 3) # Output: Hi Hi Hi

print("*" * 10) # Output: **********


# String multiplication is commonly used to create:
# - Separators
# - Patterns
# - Decorative formatting in console output

print("-" * 50) # Output: --------------------------------------------------

###################################################################################################

# RELATIONAL OPERATORS ON STRINGS

# Relational operators are used to compare strings.
#
# The result of a comparison is always: True or False

# Common relational operators:

# ==  Equal To
# !=  Not Equal To
# >   Greater Than
# <   Less Than
# >=  Greater Than or Equal To
# <=  Less Than or Equal To


# Equal To (==)

third_string = "IIM"
fourth_string = "CALCUTTA"

check = third_string == fourth_string

print(check)      # False


# Not Equal To (!=)

check_2 = third_string != fourth_string

print(check_2)    # True


# HOW PYTHON COMPARES STRINGS
#----------------------------------------------------------------------

# String comparisons are performed lexicographically.

# Lexicographical comparison means:
# Python compares characters from left to right using their Unicode values.
# Similar to how words are arranged in a dictionary.

# IMPORTANT:
# Python does NOT compare string lengths first.
# It compares characters one by one until a difference is found.


# Example 1

check_3 = "Mumbai" > "Pune"

print(check_3)    # False

# Comparison: M vs P

# Unicode: M = 77 and P = 80
# Since 77 < 80,
# "Mumbai" is considered smaller than "Pune".


# Example 2

check_4 = "Goa" < "Kolkata"

print(check_4)    # True

# Comparison: G vs K

# Unicode: G = 71 and K = 75
# Since 71 < 75,
# "Goa" is smaller than "Kolkata".

# CASE SENSITIVITY
#----------------------------------------------------------------------

# Python string comparison is CASE-SENSITIVE.

# Uppercase letters have smaller Unicode values than lowercase letters.

check_5 = "kol" < "Kol"

print(check_5)    # False

# Comparison: k vs K

# Unicode: k = 107 and K = 75
# Since 107 > 75,
# "kol" is considered greater than "Kol".

#----------------------------------------------------------------------
# IMPORTANT INTERVIEW POINT
#----------------------------------------------------------------------

# Python compares strings character by character using Unicode values.
# Length matters only when all previous characters are identical.

print("CAT" < "CATS")   # True

# Since "CAT" is a prefix of "CATS",
# the shorter string is considered smaller.

#----------------------------------------------------------------------
# QUICK SUMMARY
#----------------------------------------------------------------------

# "Apple" < "Ball"      -> True
# "A" < "a"             -> True
# "kol" < "Kol"         -> False
# "Mumbai" > "Pune"     -> False
# "CAT" < "CATS"        -> True

#############################################################################################

# Logical Operators: and | or | not

# When used with strings, Python evaluates the truthiness of the strings.
# Truthy  = Non-empty string
# Falsy   = Empty string ("")
#
# Examples:
#
# ""          -> False
# "Hello"     -> True
# "World"     -> True
# "123"       -> True
# " "         -> True (contains a space, therefore not empty)


#--------------
# LOGICAL AND
#--------------

# Rule:
# AND returns the first false value it finds.

# If all values are true, it returns the last value.

check_6 = "" and "world"

print(check_6) # Output: "", Explanation: First value is already false. Therefore Python immediately returns it.


check_7 = "Hello" and "world"

print(check_7) # Output: world, Explanation: Both strings are truthy. Therefore Python returns the last operand.


# Additional Examples

print("A" and "B")       # B
print("Python" and "AI") # AI
print("" and "AI")       # ""


#---------------
# LOGICAL OR
#---------------

# Rule:
# OR returns the first true value it finds. If all values are falsy, it returns the last value.

check_8 = "" or "world"

print(check_8)

# Output: world. Explanation: First operand is falsy. Python checks the second operand and returns it.


check_9 = "Hello" or "world"

print(check_9)

# Output: Hello. Explanation: First operand is already truthy. Python immediately returns it.


# Additional Examples

print("Python" or "AI")  # Python
print("" or "AI")        # AI
print("" or "")          # ""


#----------------------------------------------------------------------
# LOGICAL NOT
#----------------------------------------------------------------------

# Rule:
# NOT always returns a Boolean value (True or False)

check_10 = not "Hello"

print(check_10)

# Output:
# False
#
# Explanation:
# "Hello" is truthy.
# NOT reverses it.


check_11 = not ""

print(check_11)

# Output:
# True
#
# Explanation:
# Empty string is falsy.
# NOT reverses it.


#----------------------------------------------------------------------
# IMPORTANT INTERVIEW POINT
#----------------------------------------------------------------------

# AND and OR do NOT necessarily return True or False.
#
# They usually return one of the actual operands.

print("Hello" and "World")

# Output:
# World

print("" or "Python")

# Output:
# Python

# NOT is different.
# NOT always returns True or False.

print(not "Python")  # False
print(not "")        # True


#----------------------------------------------------------------------
# EASY MEMORY TRICK
#----------------------------------------------------------------------

# AND:
# Look for the first False.
# If none exist, return the last value.
#
# OR:
# Look for the first True.
# If none exist, return the last value.
#
# NOT:
# Simply reverse the truth value.