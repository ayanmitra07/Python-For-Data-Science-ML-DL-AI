#----------------------------------------------------------------------
# SECTION 19: FUNCTIONS IN PYTHON (PART 2)
#----------------------------------------------------------------------

#FUNCTION ARE 1st CLASS CITIZEN

# In Python, functions are first-class citizens because functions
# are objects and can be treated like other values such as integers, strings, or lists.

# This means a function can be:

# 1. Assigned to a variable.
# 2. Passed as an argument to another function.
# 3. Returned from another function.
# 4. Stored inside data structures such as lists and dictionaries.

#For example:

def add(a,b):
    return a + b

#Python does not execute the function body. Instead, it creates a 
# Function Object and assigns the name "add" to it:

#Global Frame --->add----------->Function Object

#For example, you can do this with an integer:
x = 10
#x -----> 10

#You can do something similar with a function:

def add(a, b):
    return a + b

x = add

#add -----> Function Object
#                ↑
#                |
#x  -------------|

#Both add and x refer to the same function object.

#And that's what the phrase "functions are first-class citizens in Python" is getting at.

#1. A function can be assigned to another variable

def square(x):
    return x ** 2

a = square #There are no parentheses after square. This implies don't call the function. Assign the function object itself to a.

print(a(5)) # Output: 25

#Because a now refers to the same function object as square.
#square ─────┐
#            ▼
#       Function Object
#            ▲
#a ──────────┘

#a = square ----> assign the function itself to a.
#a = square(5) -----> Execute the function and assign its returned result to a.

#2. A function can be passed as an argument to another function

#we can pass normal values as arguments:

def display(x):
    print(x)

display(10) #10 is passed as an argument.

#Since functions are objects, we can also pass a function itself as an argument:

def square(x):
    return x ** 2

def display(func, value):
    result = func(value)
    print(result)

display(square, 5) #output: 25

#display(square, 5) func  -----> square function object and value -----> 5
#conceptually: result = square(5) --->25

#3. A function can return another function

def outer():

    def inner():
        print("Hello")

    return inner

#When Python reads def, it creates a function object. Because that function 
# is an object, Python allows us to assign it, pass it as an argument, return it 
# from another function, and store it in data structures. That's why functions are 
# called first-class citizens in Python.

#4. Deleting a function

def square(x):
    return x ** 2
del square

print(square(4)) #output 14

del square

print(square(4)) #Output: NameError: name 'square' is not defined

#5. Storing : Just like storing a datatype we can aslos store a function. 


L= [1, 2, 3, 4, square]

print(L) #[1, 2, 3, 4, <function square at 0x000001C80DC6D440>]

L[-1](2) #output: 4

#5. FUNCTIONS AND SETS
#------------------------------------------------------------

# A set can only store hashable objects.

# A hashable object is an object for which Python can generate a hash value (an integer used for fast lookup).

# Function objects are hashable. Therefore, a function object can be stored inside a set.

s = {square}

print(s) #since the Set ran without isse it is as such function is immutable object.
#output: {<function square at 0x000001C80DC6D260>}

#Immutable built-in objects
#        ↓
#Usually hashable
#        ↓
#Can often be stored in a set

#A function is an object, and that function object is hashable, so Python allows it to be stored in a set.

#6. Returning a function
#A function can return another function because functions are first-class objects in Python.

def f():
    def x(a, b):
        return a+b
    return x
    
val = f()(3,4)
print(val) #output 7

#def → creates Function Object

#f() → creates Function Frame and executes the function

#There are actually two function calls happening one after another.

#f()       (3, 4)
# ↑           ↑
#First call   Second call

#Step 1: Python starts reading the program. It reaches def f():
#It does not execute f(). Instead, it creates a Function Object.
#
#Memory| Global Frame------>f------> Function Object


#Step 2: Python continues reading. It reaches:
#
#val = f()(3, 4)
#
#Before assigning anything to val, Python must first execute f().
#So Python creates a Function Frame for f.
#
#Memory| Global Frame------>f------> Function Object
#      |
#      ------> Function Frame (f)


#Step 3: Python starts executing the body of f().
#It reaches:
#
#def x(a, b):
#
#Python does NOT execute x().
#Instead, it creates another Function Object.
#
#Since x is defined inside f(), it belongs to the local scope of f.
#
#Memory| Global Frame------>f------> Function Object
#      |
#      ------> Function Frame (f)
#                      |
#                      ------>x------> Function Object


#Step 4: Python continues executing f().
#It reaches:
#
#return x
#
#IMPORTANT:
#There are no parentheses after x.
#
#return x       ---> Return the Function Object itself.
#return x()     ---> Call the function and return its result.
#
#Therefore, f() returns the Function Object x.


#Step 5: The Function Frame of f is destroyed.
#
#But before it is destroyed, the Function Object x has already been returned to the caller.
#
#So conceptually:
#
#f()  -------->  Function Object x


#Step 6: Now look again at the original line:
#
#val = f()(3, 4)
#
#Since f() returned the Function Object x,
#we can mentally replace f() with x.
#
#Therefore:
#
#val = f()(3, 4)
#
#becomes:
#
#val = x(3, 4)


#Step 7: Now the returned Function Object x is called with arguments 3 and 4.
#Python creates a Function Frame for x.
#
#Function Frame (x)
#        |
#        ------> a = 3
#        |
#        ------> b = 4


#Step 8: Python executes the body of x:
#
#return a + b
#
#Therefore:
#
#return 3 + 4
#
#return 7


#Step 9: The Function Frame of x is destroyed.
#The returned value 7 is assigned to val.
#
#Memory| Global Frame
#      |
#      ------> f------> Function Object
#      |
#      ------> val = 7


#Step 10: Python executes:
#
#print(val)
#
#Output:
#7

#when f() finishes, its function frame is destroyed, but the returned x function object 
# does not disappear, because the caller now has a reference to it.
# objects can survive after a frame disappears if something outside that frame still holds a reference to them. 
# In oour example, return x passes the x function object out before f's frame is destroyed. This idea becomes 
# especially important when you reach closures and decorators.

#7. Function as argument

#A function can be passed as an argument to another function.

def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_b')
    return z()

print(func_b(func_a))

#Step 1: Python starts reading the program. It reaches def func_a():
#It does not execute func_a(). Instead, it creates a Function Object.
#
#Memory| Global Frame------>func_a------> Function Object


#Step 2: Python continues reading. It reaches def func_b(z):
#Again, it does not execute func_b().
#Instead, it creates another Function Object.
#
#Memory| Global Frame------>func_a------> Function Object
#      |
#      ------>func_b------> Function Object


#Step 3: Python continues reading. It reaches:
#
#print(func_b(func_a))
#
#Before print() can execute, Python must first evaluate:
#
#func_b(func_a)
#
#IMPORTANT:
#We wrote func_a and NOT func_a().
#
#func_a     ---> refers to the Function Object itself.
#func_a()   ---> calls/executes the function.
#
#Therefore, we are passing the Function Object func_a
#as an argument to func_b.


#Step 4: Python calls func_b(func_a).
#A Function Frame for func_b is created.
#
#The Function Object func_a is received by parameter z.
#
#Memory| Global Frame
#      |
#      ------>func_a------> Function Object
#      |                          ↑
#      |                          |
#      ------> Function Frame (func_b)
#                       |
#                       ------> z
#
#Therefore, z now refers to the same Function Object as func_a.
#
#Conceptually:
#
#z = func_a


#Step 5: Python starts executing the body of func_b.
#It reaches:
#
#print('inside func_b')
#
#Output:
#inside func_b


#Step 6: Python continues executing func_b.
#It reaches:
#
#return z()
#
#Remember:
#
#z refers to the func_a Function Object.
#
#Therefore:
#
#z()
#
#is equivalent to:
#
#func_a()


#Step 7: Python calls z(), which means func_a().
#A new Function Frame for func_a is created.
#
#Memory| Global Frame
#      |
#      ------> Function Frame (func_b)
#      |                 |
#      |                 ------> z ---> func_a Function Object
#      |
#      ------> Function Frame (func_a)


#Step 8: Python starts executing the body of func_a.
#It reaches:
#
#print('inside func_a')
#
#Output:
#inside func_a


#Step 9: func_a reaches the end.
#There is no return statement.
#Therefore, Python automatically returns None.
#
#The Function Frame of func_a is destroyed.


#Step 10: Go back to this line inside func_b:
#
#return z()
#
#Since z() returned None, this becomes:
#
#return None
#
#Therefore, func_b also returns None.
#
#The Function Frame of func_b is destroyed.


#Step 11: Now return to the original line:
#
#print(func_b(func_a))
#
#Since func_b(func_a) returned None, the line becomes:
#
#print(None)
#
#Output:
#None


#Final Output:
#
#inside func_b
#inside func_a
#None

# IMPORTANT:
#
# func_a   ---> Refers to the Function Object itself.
#
# func_a() ---> Calls the function, creates a Function Frame,
#               executes the function body, and produces a return value.
#
# Therefore:
#
# func_b(func_a)
#
# passes the FUNCTION OBJECT as an argument.
#
# But:
#
# func_b(func_a())
#
# first CALLS func_a, and then passes its RETURN VALUE as an argument.

#----------------------------------------------------------------------------------------------

#8. Lambda Functions
#-------------------------------------------------------------------------------

# A lambda function is a small anonymous function created using
# the lambda keyword instead of def.

# A lambda function:
# 1. Can take any number of arguments.
# 2. Can contain only ONE expression.
# 3. Automatically returns the result of that expression.
# 4. Creates a Function Object, just like def.
# SYNTAX---> lambda parameters: expression  ------------------> lambda a, b: a + b

#Consider a normal function:

def add(a, b):
    return a + b

add(3,4) #output 7

#The equivalent lambda expression is:

lambda a, b: a + b

print(add(3, 4)) #output 7. WE called the lambda function here

#lambda     a, b      :      a + b
#  │          │       │        │
#  │          │       │        └── Expression
#  │          │       │
#  │          │       └── Separates parameters from expression
#  │          │
#  │          └── Parameters
#  │
#  └── lambda keyword

#Take two inputs, a and b, calculate a + b, and automatically return the result of its single expression.
#to use the lambda function we assign it to a variable

add = lambda a, b: a + b

result = add(3, 4)

print(result)

#MEMEORY--->

#Step 1: Python starts reading the program.
#It reaches: add = lambda a, b: a + b
#
#Python creates a Function Object. The name "add" is made to refer to that Function Object.

#Memory| Global Frame------>add------> Function Object
#The function body is NOT executed yet.


#Step 2: Python continues reading.
#It reaches: result = add(3, 4)

#Now the lambda function is called through the name add.
#Python creates a Function Frame for this function call.
#
#The arguments are received by the parameters:
#a = 3
#b = 4
#
#Memory| Global Frame------>add------> Function Object
#      |
#      ------> Function Frame
#                    |
#                    ------> a = 3
#                    |
#                    ------> b = 4


#Step 3: Python executes the single expression: a + b
#
#Therefore: 3 + 4 = 7


#Step 4: A lambda function automatically returns the result of its expression.
#
#Therefore: returns 7
#
#We do not explicitly write the return keyword in a lambda.


#Step 5: The Function Frame is destroyed.
#The returned value 7 is assigned to result.
#
#Memory| Global Frame
#      |
#      ------> add------> Function Object
#      |
#      ------> result = 7


#Step 6: Python executes:
#
#print(result)
#
#Output:
#7

#Check if a straing has 'k'

loc = lambda s:'k' in s

loc('Kolkata') #output --> True

#Check odd or even using lambda function

eod = lambda x:'even' if x%2==0 else 'odd'

eod(7) #output 'odd'

#| Feature         | Normal Function (`def`)               | Lambda Function                              |
#| --------------- | ------------------------------------- | -------------------------------------------- |
#| Name            | Usually has a defined name            | Anonymous by nature                          |
#| Keyword         | `def`                                 | `lambda`                                     |
#| Number of lines | Can contain multiple lines/statements | Limited to one expression                    |
#| Return          | Uses explicit `return`                | Automatically returns expression result      |
#| Reusability     | Designed for reuse                    | Usually used for short, temporary operations |
#| Complexity      | Can contain complex logic             | Best for simple logic                        |
#| Main use        | General-purpose functions             | Often used with Higher-Order Functions       |


#9. What is a Higher-Order Function (HOF)?
#----------------------------------------------------------------------------------------
#A Higher-Order Function is a function that does at least one of these things:

#Takes another function as an argument.
#Returns another function.

def func_b(z):
    return z(5)

result = func_b(lambda x: x ** 2)

#Step 1: Python reads def func_b(z):
#It does not execute the function. Instead, it creates a Function Object.
#Memory| Global Frame------>func_b------> Function Object


#Step 2: Python reaches:
#
#result = func_b(lambda x: x ** 2)
#
#Python first creates a lambda Function Object. Then this Function Object is passed as an argument to func_b.


#Step 3: func_b() is called.
#Python creates a Function Frame for func_b.
#
#The parameter z now refers to the lambda Function Object.
#
#Memory| Global Frame------>func_b------> Function Object
#
#       Function Frame (func_b)
#                    |
#                    ------> z------> Lambda Function Object


#Step 4: Python executes:
#
#return z(5)
#
#Since z refers to the lambda Function Object, z(5) calls the lambda function.


#Step 5: Python creates a Function Frame for the lambda function.
#
#The argument 5 is received by parameter x.
#
#Memory| Function Frame (lambda)
#                    |
#                    ------> x = 5


#Step 6: Python executes the single expression:
#
#x ** 2
#
#5 ** 2 = 25
#
#The lambda automatically returns 25.


#Step 7: The Function Frame of the lambda is destroyed.
#The value 25 goes back to func_b.


#Step 8: func_b returns 25.
#The Function Frame of func_b is destroyed.


#Step 9: The returned value is assigned to result.
#
#Memory| Global Frame
#      |
#      ------> func_b------> Function Object
#      |
#      ------> result = 25

def square(x):
  return x**2

def cube(x):
  return x**3

# HOF
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

transform(lambda x:x**3,L)

#Step 1: Python starts reading the program. It reaches def square(x):
#It does not execute square().
#Instead, Python creates a Function Object.
#
#Memory| Global Frame------>square------> Function Object


#Step 2: Python continues reading. It reaches def cube(x):
#Again, Python does not execute cube().
#It creates another Function Object.
#
#Memory| Global Frame------>square------> Function Object
#      |
#      ------>cube------> Function Object


#Step 3: Python continues reading. It reaches def transform(f, L):
#Python does not execute transform().
#Instead, it creates another Function Object.
#
#Memory| Global Frame------>square------> Function Object
#      |
#      ------>cube------> Function Object
#      |
#      ------>transform------> Function Object


#Step 4: Python reaches:
#
#L = [1, 2, 3, 4, 5]
#
#Python creates a List Object.
#The global variable L refers to that List Object.
#
#Memory| Global Frame
#      |
#      ------>square------> Function Object
#      |
#      ------>cube------> Function Object
#      |
#      ------>transform------> Function Object
#      |
#      ------>L------> [1, 2, 3, 4, 5]


#Step 5: Python reaches:
#
#transform(lambda x: x**3, L)
#
#Before transform() can execute, Python evaluates the arguments.
#
#The first argument is:
#
#lambda x: x**3
#
#Python creates a Lambda Function Object.
#
#The second argument is:
#
#L
#
#which refers to the List Object [1, 2, 3, 4, 5].


#Step 6: Python calls transform().
#A Function Frame for transform is created.
#
#The parameter f receives a reference to the Lambda Function Object.
#The parameter L receives a reference to the List Object.
#
#Memory| Global Frame
#      |
#      ------> L ------> [1, 2, 3, 4, 5]
#                         ↑
#                         |
#       Function Frame (transform)
#                    |
#                    ------> f ------> Lambda Function Object
#                    |
#                    ------> L -------|
#
#IMPORTANT:
#The global L and the parameter L inside transform()
#refer to the same List Object in this example.


#Step 7: Python starts executing the body of transform().
#It reaches:
#
#output = []
#
#Python creates an empty List Object.
#The local variable output refers to this new list.
#
#Function Frame (transform)
#        |
#        ------> f ------> Lambda Function Object
#        |
#        ------> L ------> [1, 2, 3, 4, 5]
#        |
#        ------> output ------> []


#Step 8: Python reaches:
#
#for i in L:
#
#The loop starts iterating through the list.
#
#During the first iteration:
#
#i = 1


#Step 9: Python executes:
#
#output.append(f(i))
#
#Before append() can execute, Python must first calculate:
#
#f(i)
#
#Since f refers to the Lambda Function Object:
#
#f(1)
#
#means calling:
#
#lambda x: x**3
#
#with x = 1.


#Step 10: Calling the lambda function creates a temporary Function Frame.
#
#Function Frame (lambda)
#        |
#        ------> x = 1
#
#Python executes the expression:
#
#x**3
#
#1**3 = 1
#
#The lambda automatically returns 1.
#The Lambda Function Frame is destroyed.


#Step 11: Python now executes:
#
#output.append(1)
#
#The output list becomes:
#
#[1]


#Step 12: The loop continues.
#
#Second iteration:
#i = 2
#
#f(2) creates a Lambda Function Frame.
#x = 2
#x**3 = 8
#Lambda returns 8.
#Lambda Function Frame is destroyed.
#
#output becomes:
#[1, 8]


#Third iteration:
#i = 3
#
#f(3) returns 27.
#
#output becomes:
#[1, 8, 27]


#Fourth iteration:
#i = 4
#
#f(4) returns 64.
#
#output becomes:
#[1, 8, 27, 64]


#Fifth iteration:
#i = 5
#
#f(5) returns 125.
#
#output becomes:
#[1, 8, 27, 64, 125]


#Step 13: The for loop finishes.
#Python executes:
#
#print(output)
#
#Output:
#[1, 8, 27, 64, 125]


#Step 14: transform() reaches the end.
#There is no explicit return statement.
#Therefore, Python automatically returns None.
#
#The Function Frame of transform is destroyed.
#
#The local variables:
#
#f
#L
#output
#i
#
#belonged to the transform Function Frame and are no longer available
#through that frame after the function finishes.
#
#The main program continues.
#transform() provides the general looping mechanism, while the function 
# passed into f provides the specific operation to perform on each element.
#So in this particular execution, neither square nor cube is actually used.


def square(x):
  return x**2

def cube(x):
  return x**3

# HOF
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

transform(square,L) #output: [1, 4, 9, 16, 25]

#two calls produce the same result.


#Three types of higher order function 
# -> Map, filter AND reduce

#i. map() takes a function and one or more iterables. 
#It applies that function to every item of the iterable and returns a map object.

#          Apply this function
#                       ↓
#map(         function,         iterable)
#                                  ↑
#                         Get values from here

#for example: Square the item of a list

map(lambda x:x**2,[1,2,3,4,5]) #output Creates a mao object <map object at 0x0000021AF4BB19C0>
list(map(lambda x:x**2,[1,2,3,4,5])) #output [1, 4, 9, 16, 25]

#Step 1: Python starts reading the program. It reaches:
#
#L = [1, 2, 3, 4, 5]
#
#Python creates a List Object.
#The name L refers to that List Object.
#
#Memory| Global Frame------>L------>[1, 2, 3, 4, 5]


#Step 2: Python reaches:
#
#result = list(map(lambda x: x**2, L))
#
#Before assigning anything to result, Python must evaluate
#the expression on the right side.


#Step 3: Python encounters:
#
#lambda x: x**2
#
#Python creates a Lambda Function Object.
#The lambda is NOT called yet.
#
#Conceptually:
#
#Lambda Function Object
#        |
#        ------> parameter: x
#        ------> expression: x**2


#Step 4: Python calls:
#
#map(lambda_function, L)
#
#The map object keeps what it needs to apply:
#
#1. The Lambda Function Object
#2. The iterable L
#
#Conceptually:
#
#Map Object
#    |
#    ------> Lambda Function Object
#    |
#    ------> L ------> [1, 2, 3, 4, 5]


#Step 5: The map object is passed to list().
#
#list() asks the map object for its results one by one.
#
#Now the lambda function starts being called for each element.


#Step 6: First element:
#
#x = 1
#
#Calling the lambda creates a temporary Function Frame.
#
#Function Frame (lambda)
#        |
#        ------> x = 1
#
#Python executes:
#
#x**2
#
#1**2 = 1
#
#The lambda automatically returns 1.
#The Lambda Function Frame is destroyed.


#Step 7: The same process happens for every element:
#
#x = 2 ---> returns 4
#x = 3 ---> returns 9
#x = 4 ---> returns 16
#x = 5 ---> returns 25
#
#Each lambda call gets its own temporary Function Frame.


#Step 8: list() collects all returned values:
#
#[1, 4, 9, 16, 25]
#
#The name result refers to this new List Object.
#
#Memory| Global Frame
#      |
#      ------>L------>[1, 2, 3, 4, 5]
#      |
#      ------>result------>[1, 4, 9, 16, 25]


## odd/even labelling of list items
L = [1,2,3,4,5]
list(map(lambda x:'even' if x%2 == 0 else 'odd',L)) #output ['odd', 'even', 'odd', 'even', 'odd']

#                  Is x even?
#                       ↓
#             x % 2 == 0
#                /          \
#              Yes           No
#               ↓             ↓
#            "even"         "odd"

# Fetch gender from a list of dictionaries

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

list(map(lambda user:user['gender'],users)) #output: ['male', 'male', 'female']


#filter AS HIGHER ORDER FUNCTION
# filter() is a Higher-Order Function because it accepts
# another function as an argument.

# filter() is used to SELECT items from an iterable based
# on a condition.
# numbers greater than 5
L = [3,4,5,6,7]

list(filter(lambda x:x>5,L))

# fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']

list(filter(lambda x:x.startswith('a'),fruits))

# The function is applied to every item of the iterable.

# If the function returns True:
# ---> The original item is kept.

# If the function returns False:
# ---> The original item is rejected.


# Example: Select numbers greater than 5.

L = [3, 4, 5, 6, 7]

result = list(filter(lambda x: x > 5, L))

print(result)

# Output:
# [6, 7]


# How it works:
#
# x = 3 ---> 3 > 5 ---> False ---> Reject 3
# x = 4 ---> 4 > 5 ---> False ---> Reject 4
# x = 5 ---> 5 > 5 ---> False ---> Reject 5
# x = 6 ---> 6 > 5 ---> True  ---> Keep 6
# x = 7 ---> 7 > 5 ---> True  ---> Keep 7


# MEMORY:
#
# lambda x: x > 5
#        ↓
# Creates a Lambda Function Object
#
# filter() receives:
#
# 1. The Lambda Function Object
# 2. The iterable L
#
# Each time the lambda is called for an item,
# a temporary Function Frame is created.
#
# Example:
#
# Function Frame (lambda)
#        |
#        ------> x = 6
#                    |
#                    ↓
#                 6 > 5
#                    |
#                    ↓
#                   True
#
# Because the result is True, filter() keeps the original item 6.
#
# The Lambda Function Frame is then destroyed.


#----------------------------------------------------------------------
#III. REDUCE AS A HIGHER-ORDER FUNCTION
#----------------------------------------------------------------------

# reduce() is a Higher-Order Function because it accepts another
# function as an argument.

# Unlike map() and filter(), reduce() is not directly available as
# a built-in function. It is available inside the functools module.

import functools


# SYNTAX:

# functools.reduce(function, iterable)


# reduce() repeatedly combines items from an iterable until
# only ONE final accumulated value remains.


#----------------------------------------------------------------------
# EXAMPLE 1: SUM OF ALL ITEMS
#----------------------------------------------------------------------

result = functools.reduce(
    lambda x, y: x + y,
    [1, 2, 3, 4, 5]
)

print(result)

# Output:
# 15


# Execution:
#
# x = 1,  y = 2  ---> 1 + 2  = 3
#
# x = 3,  y = 3  ---> 3 + 3  = 6
#     ↑
#     Previous result
#
# x = 6,  y = 4  ---> 6 + 4  = 10
#
# x = 10, y = 5  ---> 10 + 5 = 15
#
# Final result = 15


# IMPORTANT:
#
# After the first operation:
#
# x = accumulated result from the previous operation
# y = next item from the iterable


#----------------------------------------------------------------------
# EXAMPLE 2: FIND MAXIMUM
#----------------------------------------------------------------------

numbers = [23, 11, 45, 10, 1]

maximum = functools.reduce(
    lambda x, y: x if x > y else y,
    numbers
)

print(maximum)

# Output:
# 45


#----------------------------------------------------------------------
# EXAMPLE 3: FIND MINIMUM
#----------------------------------------------------------------------

minimum = functools.reduce(
    lambda x, y: x if x < y else y,
    numbers
)

print(minimum)

# Output:
# 1


#----------------------------------------------------------------------
# MEMORY
#----------------------------------------------------------------------

# lambda creates a Function Object.
#
# reduce() receives:
#
# 1. The Lambda Function Object
# 2. The iterable
#
# Each time reduce() calls the lambda:
#
# A temporary Function Frame is created.
#
# Example:
#
# Function Frame (lambda)
#        |
#        |----> x = accumulated result
#        |
#        |----> y = next item
#
# The lambda executes its expression and automatically returns a result.
#
# That result becomes x for the next call.
#
# The Lambda Function Frame is destroyed after each call.
#
# This continues until all items have been processed.
#
# reduce() finally returns ONE accumulated value.