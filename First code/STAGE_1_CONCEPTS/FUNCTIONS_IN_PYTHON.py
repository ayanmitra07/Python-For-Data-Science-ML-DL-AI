#----------------------------------------------------------------------
# SECTION 19: FUNCTIONS IN PYTHON (PART 1)
#----------------------------------------------------------------------

# What is a Function?
#----------------------------------------------------------------------
# A function is a reusable block of code that performs a specific task.
# It can take inputs (parameters), process them, and optionally return an output.
 
# Functions help avoid writing the same code repeatedly.Example:
# print(), len(), input(), type() are built-in functions.


# Types of Functions
#----------------------------------------------------------------------

# 1. Built-in Functions -> Functions already provided by Python. Examples:
# print() | len() | type() | input() | sum()| max()

# 2. User-defined Functions:>  Functions created by the programmer according to the application's needs.
# Examples:
# Login function
# Registration function
# Search function
# Even/Odd checker


# Advantages of Functions
#----------------------------------------------------------------------

# 1. Code Reusability -> Write once, use many times.

# 2. Better Readability -> Code becomes easier to understand.

# 3. Easier Maintenance -> Changes need to be made in only one place.

# 4. Modularity -> Large programs are divided into smaller independent functions.


# Two Important Principles
#----------------------------------------------------------------------

# 1. Abstraction -> The user only knows WHAT the function does, not HOW it does it.
# Example: print("Hello")
#
# We know it prints text, but we don't know its internal implementation.

# 2. Decomposition -> Breaking a large problem into smaller functions.
#
# Example:
# Main Program
# ├── login()
# ├── search()
# ├── payment()
# └── logout()


# Components of a Function
#----------------------------------------------------------------------

def is_even(i):
    """
    Returns True if the given number is even,
    otherwise returns False.
    """

    x = (i % 2 == 0)

    return x


# Explanation
#----------------------------------------------------------------------

# def -> Keyword used to define a function.

# is_even -> Function Name

# (i) Parameter -> A parameter is the variable that receives the input.

# : -> Indicates the start of the function body.

# Docstring ->
# A multiline string enclosed within triple quotes.
# It explains what the function does,
# its inputs, outputs, and purpose.
# It acts as the function's documentation.

# Body -> Contains the logic of the function.

# return ->
# Sends the result back to the function caller.
# Once 'return' executes, the function immediately stops.


# Calling a Function
#----------------------------------------------------------------------

is_even(7)

# Here: 7 is called the Argument. The function executes only when it is called.


# Parameter vs Argument
#----------------------------------------------------------------------

# Parameter: Variable defined inside the function definition.

def square(x):
    return x * x

# x is the parameter.

# Argument: Actual value passed while calling the function.

square(5)

# Here: 5 is the argument.
######################################################################################################

#Lets create a function(with docstring) -> is_even()

def is_even(num):
  """
  This function returns if a given number is odd or even
  input - any valid integer
  output - odd/even
  created on - 1st Jul 2026
  """
  if num % 2 == 0:
     return 'even'
  else:
     return 'odd'

#Lets use the function /calling the function ->is_even

#function_name(input)

for i in range(1,11):
   x = is_even(i)
   print(x)

#Two point of view
#--------------------------------

#There are two point of view one from the senior programmer creating the python function program another is the junior 
#programmer using the created function

#if there is some error in the function the senior programmer must make the program such that those error can be handled.

#Whenever we design a function we need to factor for any error else the mistake is on our part. 
# we need to make sure such error do not happen

#so to factor in any error we can do the below when we are creating a program

def is_even(num):
  """
  This function returns if a given number is odd or even
  input - any valid integer
  output - odd/even
  created on - 1st Jul 2026
  """
  if type(num) == int:
     if num % 2 == 0:
        return 'even'
     else:
        return 'odd'
  else:
    return "Wrong entry type"
  
#ACCESSING DOCUMENTATION

is_even.__doc__
#Output: '\n  This function returns if a given number is odd or even\n  input - any valid 
# integer\n  output - odd/even\n  created on - 1st Jul 2026\n  '

print(type.__doc__)
print(print.__doc__)
  
#TYPES OF ARGUMENTS
#-----------------------------------------------------------
#There are few ways to send an argument

#Default Argument               #Positional Argument            #Keyword Argument

# 1. DEFAULT ARGUMENTS
#--------------------------------------------------------------------

# Default arguments allow us to assign default values to function parameters.
# If the caller does not provide a value for that respective argument, Python 
# automatically uses the default value from the parameters.

# Example:
# Create a function that returns a raised to the power of b.

# Function without default arguments

def power(a, b):
    return a ** b

# Calling the function

print(power(2, 3))      # Output: 8

# If one argument is missing, Python raises an error because both parameters are required.

power(5) # TypeError: power() missing 1 required positional argument: 'b'


# Function with default arguments

def power(a=1, b=1):
    return a ** b

print(power(5))      # Output: 5 -> Equivalent to: power(5, 1)

print(power())       # Output: 1 -> Equivalent to: power(1, 1)

print(power(2, 3))   # Output: 8 Default values are ignored because both arguments are supplied.

# 2. POSITIONAL ARGUMENTS
#--------------------------------------------------------------------

# In positional arguments, values are assigned to parameters
# based on their position (order).

#Positional arguments are arguments that are assigned to function parameters based on their 
# position during the function call. 
# The order of arguments must match the order of the parameters.

# The first argument is assigned to the first parameter,
# the second argument to the second parameter,
# and so on.

def power(a, b):
    return a ** b

print(power(2, 3))   # a = 2, b = 3
# Output: 8

print(power(3, 2))   # a = 3, b = 2
# Output: 9

# Since positional arguments depend on order,
# changing the order of arguments changes the result.

# 3. KEYWORD ARGUMENTS
#--------------------------------------------------------------------

# In keyword arguments, we explicitly specify the parameter name
# while passing the argument.

# Since each argument is assigned using its parameter name,
# the order of arguments does not matter.

# Keyword arguments are especially useful when a function has
# many parameters, making the code more readable.

def power(a, b):
    return a ** b

# Using keyword arguments

print(power(b=3, a=2))    # Output: 8

# Equivalent to:
# a = 2
# b = 3

# Since parameter names are specified,
# Python correctly assigns the values regardless of their order.

#Real-world Example (Very Common)

#Instead of remembering the position of sklearn. DecisionTreeClassifier which has multiple parameter
# we can simplyvprovide the parameter name.

#sklearn.DecisionTreeClassifier(criterion="gini",max_depth=10, min_samples_split=2)

#One Important Rule: You can mix positional and keyword arguments, 
# but positional arguments must come first.

power(2, b=3) #output 8

#power(a=2, 3) #output SyntaxError: positional argument follows keyword argument

#---------------------------------------------------------------------------------------------------------------

#*args and **kwargs
#---------------------------------------------
#*args and **kwargs are special Python keywords that are used to pass the 
# variable length of arguments to a function
#in other words we can panss any number of arguments

# *args and **kwargs
#--------------------------------------------------------------------

# *args and **kwargs are special Python syntax used to pass
# a variable number of arguments to a function.

# They are useful when we do not know beforehand
# how many arguments will be passed.

# 1. *args
#--------------------------------------------------------------------

# *args allows a function to accept a variable number
# of POSITIONAL arguments. in other words allows us to pass non keyword arguments

# Example: Create a function that returns the multiplicationof three numbers.

def multiple(a, b, c):
    return a * b * c

print(multiple(2, 3, 5))      # Output: 30

# The above function works only when exactly three arguments are supplied.

# If the number of inputs is unknown,*args can be used.

def multiple(*args):

    product = 1

    # args is a tuple containing all positional arguments.

    print(args)      # (5, 4, 3, 2, 1)

    for i in args:
        product *= i #product = product * i

    return product

print(multiple(5, 4, 3, 2, 1))      # Output: 120
#We can use any variable with a single * mark to do this work it is not required to mention args
# The '*' is mandatory.
# The name after '*' can be anything.
#args is just a convention. The * is what tells Python to collect all positional arguments into a tuple.
#----------------------------------------------------------------------------------------------------------

# **kwargs
#-------------------------------------
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.
#** indicated the pairs we sent will be converted to dictionary

#Keyword arguments are passed in the form:
# parameter_name = value

# Python automatically collects all keyword arguments
# into a dictionary.

# '**kwargs' is only a naming convention.
# The '**' is mandatory, but the variable name can be anything.

def display(**countries):

    print(countries)

    for key, value in countries.items():
        print(key, "->", value)

display(
    india='delhi',
    srilanka='colombo',
    nepal='kathmandu',
    pakistan='islamabad'
)

#Points to remember while using *args and **kwargs
#order of the arguments matter(normal -> *args -> **kwargs)
#The words “args” and “kwargs” are only a convention, you can use any name of your choice

#-----------------------------------------------------------------------------------------------------------

#Q.How Functions are executed in memory?

#In Python, executing the program simply means: Python reads the file from top
#to bottom and performs the action required for each line.
# Not every line means "run some logic." Different lines have different actions.

x = 10

def add(a, b):
    c = a + b
    return c

y = 20

print(add(x, y))

#Python is reading the file line by line
#1. Python executes the line x = 10. Here executes means storing in memory x -----> 10

#2. In the next line Python executes def add(a, b):
#here it is not "run the function." Instead, the action is: Create a function object named add.
#Memory now becomes: x -------> 10          add -----> Function Object 
#The function body is simply stored inside that object

#3. Python does not do the below lines because nobody has called the function yet.
# c = a + b
# return c
#Then Python continues reading the next line after the function definition.

#4. Python executes y = 20, 
#Memory: x -------> 10          y -------> 20           add -----> Function Object

#5. Python continues executing the program until it encounters a function call print(add(x, y)).
#When the function is called (inside print in this case), Python creates a function frame.

#6. Python needs to know what add(x, y) returns so it starts executing it.

#7. Only now does Python create a function frame.
# a = 10
# b =20
#then it executes c = a + b

#Then returns c

#8. The function frame is destroyed.

#def
#│
#├── Creates a Function Object (once)
#│
#└── Does NOT execute the function

#Function Call

#add(10,20)

#│
#├── Creates a Function Frame
#├── Executes the function
#├── Returns the result
#└── Deletes the frame

#-----------------------------------------------------------------------------------------------

#. What happens to a function without a return statement?

def is_even(num):


  if num % 2 == 0:
     print('even')
  else:
     print('odd')

print(is_even(7))

#Step 1 Python creates the function object. Nothing is printed yet.

#step 2 Python reaches print(is_even(7))

# Before print() can execute, it must evaluate is_even(7)

#Step 3 A function frame is created. num = 7

#Step 4: Python executes if num % 2 == 0: 
#Since 7 % 2 = 1 the condition is False.
#So Python executes print("odd") Output: odd

#Step 5 Now Python reaches the end of the function.

#There is no return statement.

#Whenever Python reaches the end of a function without a return, it automatically returns None by default

#So internally, Python behaves as if you had written:

def is_even(num):

    if num % 2 == 0:
        print("even")
    else:
        print("odd")

    return None

print(is_even(7))

#Step 6 So is_even(7) returns none

# If a function reaches the end without executing a return statement,
# Python automatically returns None.

#One important distinction to remember
#print() displays a value on the screen.
#return sends a value back to the caller.

#For example:

def square(x):
    print(x * x)

#prints the square but returns None.

#Whereas:
def square(x):
    return x * x

#doesn't print anything by itself—it returns the computed value so the caller can print it, 
# store it, or use it in another calculation.

L = [1, 2, 3]

print(L.append(4)) #output None.
print(L) #output [1, 2, 3, 4]

#-------------------------------------------------------------------------------------------------------

#4. VARIABLE SCOPE
#--------------------------------
#Variable scope is the region of a program where a variable can be accessed.

#Python has two scopes that you'll learn first:

#Global Scope → Variables created outside a function.
#Local Scope → Variables created inside a function.

#CASE 1->
def g(y):
   print(x)
   print(x+1)
x = 5
g(x)
print(x)

#When the function starts executing it will first read def creates a function object 
# then immediately shift to the line x =5
#A program block is created, and a variable is created x whose value is 5
#in the next line we call the function g(x) and send x as input, the moment we execute this line a 
#scope for the function will be created. under this scope the value for y will be 5.
#the main program scope is for when we create for g(x) also called the global variable
#on the other hand function scope created for def will come for y as 5.this is local variable
#Local variable can only be found inside the user define function scope not outside, the main
#program cannot use the locav variable.
#on the other hand the global variable can be used under the user defined function under the local variable
#global variable comes under the scope of the program
#local variable comes under the scope of function, under the local scope we can use global variable but not the other way around

#in the second line of the program, print(x), the execution is now within the user defined function,
#where there is no x within the function scope directly, as a result the python's interpreter will go to the global
#scope to find if there are any variable eith respect to the scope of global
#SInce the variable is there it will print -> 5
#now within the user defined function body we move on to the next line print(x+1)
#the interpreter find x on a global variable in the programs perspective and hence print -> 6
# Since there is nothing more in the function so by default it return none
# In line g(x), we are not storing anything so the none dissapers.
# In the final line we again have print(x) and since on a global variable x =5 it will print 5 

#Step 1: Python reads def g(y): and creates a Function Object but Nothing executes inside it.
#inside the Memory | Global Frame -------g -----> Function Object

#Step 2: Python reads x = 5
#inside memory| Global Frame--------------->g -----> Function Object and x -----> 5
#Here x is created outside the function. therefore x is a Global Variable. 

#Step 3: Python reaches g(x). Now Python creates a Function Frame.
#Therefore, Global Frame----------> x
#and        Function Frame -------> y

#Step 4: Now python executes print(x)
#Inside the function. Immediately Python asks "Where is x?"
#It first searches Function Frame where it find y = 5 and no x
#Then it searches Global Frame and find x =5, thus print 5

#Step 5: Next line print(x+1)
#python again searches for x but unables to find it in  local frame
#it searches in the global frame and find x = 5 and thus calculates 5+1 = 6

#Step 6:  End of function. No return statement. Python automatically returns None.
#But g(x) doesn't store the return value. So None is discarded.
#Then Function Frame is destroyed.
#Only Global Frame x = 5 remains.

#Step 7: Python executes print(x)
#Looks inside Global Frame and finds x = 5 and thus prints 5

#final output 5|6|5

#Python follows a search order
#I need variable x.--->Step 1:Is x inside the current function?----->No
#---> Step 2: Is x in the global program?---->yes--->uses it
#That search process is called LEGB Rule.

#A local scope can access variables from the global scope.
#However, the global scope cannot directly access local variables created inside a function.

# Example explaining variable shadowing:
# this program is designed to show that a local variable hides (shadows) a global variable with the same name.

def f(y):
    x = 1
    x += 1
    print(x)
x = 5
f(x)
print(x)

#Step 1:Python reads def f(y): and creates a function object.
#In Memory| Global Frame----------------->f -----> Function Object

#Step 2: Python executes x = 5
#In memory| Global Frame ----->f -----> Function Object
#and                     ----> x = 5--> global variable.

#Step 3: Python reaches f(x) and thus it creates a function frame.
#Arguments are copied. Global Frame ---> x= 5 copied to Function frame y = 5
#There is only y inside the function right now. There is no local x yet.

#Step 4: Python executes x = 1, and inside the function, Python sees an assignment to x.
#Create a new local variable called x.
#Now memory becomes| Global Frame ---->x=5
#and               | Function Frame----->y = 5 and x = 1
#Now there are two different variables named x which are independent of each other.

#Step5: Python executes x += 1
#here, x is not the global variable x=5, but it is the local variable where x =1 currently.
#Python always checks the local scope first. So x =x+1 becomes x=2
#Memory| Global Frame---->x=5
#and   | Function Frame-----> y =5 and x =2
#The global x never changes.

#Step 6: Python executes print(x) within the function body and searches for x in Local first
#Local Frame x=2, Output 2

#Step 7: Python reaches the end of the function. There is no return statement.
#So Python automatically does --->return None
#The function frame is destroyed.
#Memory now becomes| Global Frame---->x=5
#and                f -----> Function Object 

#Everything inside the function disappears. Local x and local y is deleted

#Step 8: Python continues executing the program. It reaches print(x)
#There is no function frame anymore. Only the Global Frame exists.
#Global Frame x=5, therefore the output is 5

#Final Output---> 2| 5
#-------------------------------
#ANOTHER EXAMPLE
def h(y):
    x += 1

x = 5

h(x)

print(x)

#Step 1: Python reads def h(y): It creates a Function Object.
#Memory| Global Frame-------> h -----> Function Object

#Step 2:Python executes x = 5
#Memory| Global Frame----->h -----> Function Object 
#AND                 ------> x = 5 (GLOBAL VARIABLE)

#Step 3: Python executes h(x) A Function Frame is created.
#Argument is copied. Global Frame ---->x = 5 copied to Function frame y =5

#Step 4:Python starts executing x += 1
# This is where everyone think there is no local x, so Python should go to the global x
#That would seem logical, but that's NOT what Python does

#Python first rewrites x += 1 as x =x +1
# x = x + 1 is an assignment to x
#Because there is an assignment, Python decides, x is going to be a LOCAL variable in this function.
#This decision is made before the function starts running.

#Now Python tries to execute x = x + 1
#It evaluate the right side first x + 1 and thus starts to look for local x
#within the Function Frame we have y = 5

#previously Python already decided that x is local because of the assignment.
#So it does not look at the global x. and thus it returns an error

#Q. Why doesn't Python use the global x?
#Because the line x += 1 contains an assignment operator.
#Any assignment inside a function makes that variable local, unless we explicitly tell Python otherwise.


#The correct way is to explicitly mention global but this is not a good programming practise

x = 5

def h(y):

    global x

    x += 1

h(x)

print(x)
#-----------------------------------------------------------------------------
def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)
#-----------------------------------------------------------------------------

#5. NESTED FUNCTIONS
#--------------------------------------------------

def f():

    def g():
        print("inside function g")

    g()

    print("inside function f")

f()

#Step 1: Python starts reading the program. It reaches def f():
#It does not execute f(). Instead, it creates a Function Object.
#Memory| Global Frame------>f------> Function Object

#Step 2: Python continues reading. It reaches f().
#Now Python creates a Function Frame for f.
#MEMORY|Global Frame------>f
#and   |Function Frame (f)
#Now Python starts executing the body of f.

#Step 3: Inside f, Python reaches def g():
#Again, Python does not execute g. Instead it creates another Function Object.
#But unlike f, this function belongs to the local scope of f.
#Memory becomes: Global Frame---->f
#and Functional frame(f)----> g -----> Function Object
#g is not created in the global frame. It is created inside the function frame of f. So g is a local function.

#Step 4: Python continues executing f. It reaches g()
#Now Python creates another Function Frame. Global Frame|----> Function Frame (f)---->Function Frame (g)
#Now the body of g executes. print("inside function g")| Output ----> inside function g

#Step 5: g reaches the end. No return statement. So Python automatically does return None
#The Function Frame of g is destroyed.
#Memory|Global Frame---->Function Frame (f)

#Step 6: Python continues executing f. print("inside function f"). Output--->inside function f

#Step 7: f reaches the end. No return. Python returns None. The Function Frame of f is destroyed.
#Memory|Global Frame-------> f -----> Function Object
#The function object g also disappears because it only existed inside f's frame.

#Final Output :inside function g| inside function f

#Example: A function with three scope

#Global Scope
#Local Scope of g()
#Local Scope of h()

def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)

##Step 1: Python starts reading the program. It reaches def g(x):
#It does not execute g(). Instead, it creates a Function Object.
#Memory| Global Frame------>g------> Function Object


#Step 2: Python continues reading. It reaches x = 3.
#Python creates a global variable x whose value is 3.
#Memory| Global Frame------>g------> Function Object
#      |                 |
#      |                 ------> x = 3


#Step 3: Python continues reading. It reaches z = g(x).
#Before assigning anything to z, Python must execute g(x).
#Python creates a Function Frame for g.
#The argument x = 3 is copied into the parameter x.
#
#Memory| Global Frame------>g------> Function Object
#      |                 |
#      |                 ------> x = 3
#      |
#      ------> Function Frame (g)
#                      |
#                      ------> x = 3 (Local Variable)
#
#Notice:
#There are now two different variables named x.
#One belongs to the Global Frame.
#The other belongs to the Function Frame of g.


#Step 4: Python starts executing the body of g().
#It reaches def h():
#Python does not execute h(). Instead, it creates another Function Object.
#Since h is defined inside g(), it belongs to the local scope of g.
#
#Memory| Global Frame------>g------> Function Object
#      |
#      ------> Function Frame (g)
#                      |
#                      ------> x = 3
#                      |
#                      ------> h------> Function Object


#Step 5: Python continues executing g().
#It reaches x = x + 1.
#Python first looks for x in the local scope.
#It finds Local x = 3.
#It calculates 3 + 1 and stores the result back into the local variable.
#
#Memory| Global x = 3
#      |
#      ------> Function Frame (g)
#                      |
#                      ------> x = 4
#
#Notice:
#The Global x is still 3.
#Only the Local x inside g has changed.


#Step 6: Python executes
#print('in g(x): x =', x)
#
#Python again searches the Local Scope first.
#It finds x = 4.
#
#Output:
#in g(x): x = 4


#Step 7: Python continues executing g().
#It reaches h().
#Python creates a Function Frame for h.
#
#Memory| Global Frame
#      |
#      ------> Function Frame (g)
#      |
#      ------> Function Frame (h)


#Step 8: Python starts executing h().
#It reaches x = 'abc'.
#Since this assignment happens inside h(),
#Python creates a brand new Local Variable x.
#
#Memory| Global x = 3
#      |
#      ------> Function Frame (g)
#      |               |
#      |               ------> x = 4
#      |
#      ------> Function Frame (h)
#                      |
#                      ------> x = 'abc'
#
#Notice:
#There are now THREE completely different variables named x.
#
#Global x = 3
#Local x inside g = 4
#Local x inside h = 'abc'


#Step 9: h() reaches the end.
#There is no return statement.
#Python automatically returns None.
#The Function Frame of h is destroyed.
#
#Memory| Global Frame
#      |
#      ------> Function Frame (g)
#                      |
#                      ------> x = 4
#
#The local variable x = 'abc' disappears because
#it only existed inside h().


#Step 10: Python continues executing g().
#It reaches return x.
#Python searches the Local Scope first.
#It finds x = 4.
#It returns 4.
#
#The Function Frame of g is destroyed.


#Step 11: The returned value (4) is assigned to z.
#
#Memory| Global Frame
#      |
#      ------> g------> Function Object
#      |
#      ------> x = 3
#      |
#      ------> z = 4


#Final Output:
#in g(x): x = 4
#
#Final Memory:
#Global x = 3
#Global z = 4


#Important Observation:
#
#Although all three variables have the same name (x),
#they are completely different variables because they belong
#to different Function Frames (Scopes).
#
#Global Frame  ---> x = 3
#Function g()  ---> x = 4
#Function h()  ---> x = 'abc'
#
#Changing one x does not affect the others.

#Example

def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)


#Step 1: Python starts reading the program. It reaches def g(x):
#It does not execute g(). Instead, it creates a Function Object.
#Memory| Global Frame------>g------> Function Object


#Step 2: Python continues reading. It reaches x = 3.
#Python creates a global variable x whose value is 3.
#Memory| Global Frame------>g------> Function Object
#      |                 |
#      |                 ------> x = 3


#Step 3: Python continues reading. It reaches z = g(x).
#Before assigning anything to z, Python must execute g(x).
#Python creates a Function Frame for g.
#The argument x = 3 is copied into the parameter x.
#
#Memory| Global Frame------>g------> Function Object
#      |                 |
#      |                 ------> x = 3
#      |
#      ------> Function Frame (g)
#                      |
#                      ------> x = 3 (Parameter / Local Variable)


#Step 4: Python starts executing g().
#It reaches def h(x):
#Python does not execute h().
#Instead, it creates another Function Object.
#Since h is defined inside g(),
#it belongs to the local scope of g.
#
#Memory| Global Frame------>g------> Function Object
#      |
#      ------> Function Frame (g)
#                      |
#                      ------> x = 3
#                      |
#                      ------> h------> Function Object


#Step 5: Python continues executing g().
#It reaches x = x + 1.
#Python searches the local scope first.
#It finds Local x = 3.
#It calculates 3 + 1.
#The Local x becomes 4.
#
#Memory| Global x = 3
#      |
#      ------> Function Frame (g)
#                      |
#                      ------> x = 4


#Step 6: Python executes
#print('in g(x): x = ', x)
#
#Python finds Local x = 4.
#
#Output:
#in g(x): x = 4


#Step 7: Python continues executing g().
#It reaches h(x).
#Python creates a Function Frame for h.
#
#The current value of Local x (which is 4)
#is copied into h's parameter x.
#
#Memory| Global Frame
#      |
#      ------> Function Frame (g)
#      |               |
#      |               ------> x = 4
#      |
#      ------> Function Frame (h)
#                      |
#                      ------> x = 4 (Parameter)


#Notice:
#The parameter x of h() is itself a Local Variable.
#Python does NOT use g's x directly.
#Instead, it copies the value into h's parameter.


#Step 8: Python starts executing h().
#It reaches x = x + 1.
#Python searches the Local Scope of h.
#It finds x = 4.
#It calculates 4 + 1.
#The Local x inside h becomes 5.
#
#Memory| Global x = 3
#      |
#      ------> Function Frame (g)
#      |               |
#      |               ------> x = 4
#      |
#      ------> Function Frame (h)
#                      |
#                      ------> x = 5


#Step 9: Python executes
#print("in h(x): x = ", x)
#
#Output:
#in h(x): x = 5


#Step 10: h() reaches the end.
#There is no return statement.
#Python automatically returns None.
#The Function Frame of h is destroyed.
#
#Memory| Global Frame
#      |
#      ------> Function Frame (g)
#                      |
#                      ------> x = 4
#
#Notice:
#Changing x inside h() did NOT change x inside g().
#Because they belong to different Function Frames.


#Step 11: Python continues executing g().
#It reaches return x.
#Python searches the Local Scope.
#It finds x = 4.
#It returns 4.
#
#The Function Frame of g is destroyed.


#Step 12: The returned value is assigned to z.
#
#Memory| Global Frame
#      |
#      ------> g------> Function Object
#      |
#      ------> x = 3
#      |
#      ------> z = 4


#Step 13: Python executes
#print('in main program scope: x = ', x)
#
#Python searches the Global Scope.
#It finds x = 3.
#
#Output:
#in main program scope: x = 3


#Step 14: Python executes
#print('in main program scope: z = ', z)
#
#Python searches the Global Scope.
#It finds z = 4.
#
#Output:
#in main program scope: z = 4


#Final Output:
#in g(x): x = 4
#in h(x): x = 5
#in main program scope: x = 3
#in main program scope: z = 4

#In your previous example, h() had no parameters, so it created its local x with: x = "abc"
#In this example, h(x) already has a local variable the moment the function starts, 
# because parameters are local variables. When you call h(x), Python copies the 
# value 4 into h's parameter x. Then x = x + 1 changes only that local parameter, not g's x. 
# This is an important distinction and is commonly tested in interviews.