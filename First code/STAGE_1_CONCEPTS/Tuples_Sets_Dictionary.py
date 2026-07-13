#----------------------------------------------------------------------
#SECTION 16: TUPLES IN PYTHON
#----------------------------------------------------------------------
#A tuple in Python is similar to a list. The difference between the two is that we cannot change 
# the elements of a tuple once it is assigned whereas we can change the elements of a list.

#In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.

#Characterstics

#Ordered
#Unchangeble
#Allows duplicate


#PLAN OF ACTION
#------------------------------------
#Creating a Tuple
#Accessing items
#Editing items
#Adding items
#Deleting items
#Operations on Tuples
#Tuple Functions

#1.Creating a Tuple
#------------------------------------------------

#empty tuple

t1 = ()
print(t1)

#2.Creating tuple with single item
#------------------------------------------------

t2 = (2)

print(t2) #outputs: 2 which is an intiger
print(type(t2))#outputs: <class 'int'>

#we need to add a comma after our item so that it is considered as a single item tuple

t3 = ('Hello',)
print(t3) #outputs: ('Hello',)
print(type(t3)) #outputs: <class 'tuple'>

#3. Creating a homogeneous tuple
#-----------------------------------------------

t4 = (1, 2, 3, 4)

print(t4) #Outputs: (1, 2, 3, 4)

#4. Creating heterogenious tuple
#-----------------------------------------------

t5 = (1, 2.5, True, "Ayan", [4, 2.5, "Answer"])

print(t5) #Outputs: (1, 2.5, True, 'Ayan', [4, 2.5, 'Answer'])
print(type(t5)) #outputs: <class 'tuple'>

#5. Creating Nested tuple
#-----------------------------------------------

t6 = (1, 2, 3, (4, '3.5'))
print(t6) #outputs: tuple-> (1, 2, 3, (4, '3.5'))
print(type(t6)) #Outputs: <class 'tuple'>

#6. Creating tuple using type conversion
#-----------------------------------------------
t7 = tuple('Ayan Mitra')
print(t7) #Creates tuple -> ('A', 'y', 'a', 'n', ' ', 'M', 'i', 't', 'r', 'a')

#Accessing Items
#Indexing
#Slicing
#-------------------------------------------------------------------------------

#We can access items in tuple just like a list

t4 = (1, 2, 3, 4)

#Indexing feteches one item at a time
print(t4[0]) #Using Positive Indexing to access the first item, Outputs: 1

print(t4[-1]) #Using Negative Indexing to access the last item, Outputs: 4

#Slicing fetches multiple items at a time

print(t4[0:3]) #outputs (1, 2, 3)

print(t4[0:4:2]) #outputs alternate items (1, 3)

print(t4[-3:-2]) #outputs (2,)

print(t4[-3:-1]) #outputs (2, 3)

print(t4[-3::2]) #outputs: (2, 4)

print(t4[-3:]) #outputs: (2, 3, 4)

print(t4[::-1]) #outputs: (4, 3, 2, 1)

print(t4[-1:-4:-1]) #outputs: (4, 3, 2) |when we want to reduce we need to keep the lesser number at the beggining

#Extracting items from a 2d list

t6 = (1, 2, 3, (4, '3.5'))

print(t6[3][1]) #outputs: 3.5

#EDIT ITEMS IN TUPLES
#------------------------------------------------
# immutable just like strings
print(t4)
t4[0] = 100 #ypeError: 'tuple' object does not support item assignment

#Adding items
#------------------------------------------------
print(t4)
# not possible

#Deleting items - We can delete the entire tuple but not just a portion of it
#-------------------------------------------------

print(t4) #output: (1, 2, 3, 4)
del t4
print(t4) #outputs NameError: name 't4' is not defined.

#Deleting portion of the tuple will not work as it worked before in list

print(t6) #outputs: (1, 2, 3, (4, '3.5'))
del t6[-1] #outputs: TypeError: 'tuple' object doesn't support item deletion

#OPERATIONS IN TUPLE
#-----------------------------------------------------

# + and *
t1 = (1,2,3,4)
t2 = (5,6,7,8)

print(t1 + t2) #Output: Concatinates the tuples(1, 2, 3, 4, 5, 6, 7, 8)
print(t1 * 3) #output: muliplies the elements by the scalar value (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

#Membership

1 in t1 #output: True

#Iteration

for i in t1:
    print(i)

#TUPLE FUNCTION
#-------------------------------------------------

#1. Length 
t = (2, 4, 5.2, True, (6, 'Ed'), 'BATMAN')

print(len(t)) #output: 6 items

#2. SUM 
s = (6, 5, 1, 2)

print(sum(s)) #output: 14

#3. min

min(s) #output: 1

#4. max

max(s) #output: 6

#5. sorted

print(sorted(s)) #Output: [1, 2, 3, 4] sorted() always returns a new list, 
                    #regardless of whether the input is a tuple, string, set, or list.

sorted(s, reverse = True) # outputs the reverse list [6, 5, 2, 1]

print(type(s))

sorted(t)

#6.count

c = (4, 5, 7, 8, 1, 4, 6)

c.count(4)  #Outputs: 2 . Provides the no. of counts for the item mentioned 

#6.INDEX : Provides the index position of the item

c.index(8) #Output: index position of 8 -> 3


# DIFFERENCE BETWEEN LISTS AND TUPLES
#------------------------------------------------------------------

# Lists and Tuples are both sequence data types in Python.
# Both can store multiple values and support indexing, slicing, loops, etc.

# 1. SYNTAX
#------------------------------------------------------------------

# List uses square brackets []

L = [1, 2, 3]

# Tuple uses round brackets ()

T = (1, 2, 3)

# Single element tuple requires a comma

T1 = (5,)   # Correct

T2 = (5)    # This is an integer, not a tuple

print(type(T1))  # <class 'tuple'>
print(type(T2))  # <class 'int'>


# 2. MUTABILITY
#------------------------------------------------------------------

# List is Mutable -> values can be changed

L = [1, 2, 3]
L[0] = 100

print(L)  # [100, 2, 3]

# Tuple is Immutable -> values cannot be changed

T = (1, 2, 3)

# T[0] = 100
# TypeError: 'tuple' object does not support item assignment


# 3. SPEED
#------------------------------------------------------------------

# Tuples are generally faster than Lists

# Reason:
# Tuples are immutable.
# Python does not need to allocate extra memory for modifications.

# Therefore:
# Tuple access is slightly faster than List access.


# 4. MEMORY
#------------------------------------------------------------------

# Tuples consume less memory than Lists

L = [1, 2, 3]
T = (1, 2, 3)

# Since Lists are mutable,
# Python allocates extra memory for future modifications.

# Tuples are fixed-size objects,
# therefore they require less memory.


# 5. BUILT-IN FUNCTIONALITY
#------------------------------------------------------------------

# Lists have many built-in methods

L = [1, 2, 3]

# L.append()
# L.extend()
# L.insert()
# L.remove()
# L.pop()
# L.sort()
# L.reverse()

# Tuple has very few methods

T = (1, 2, 3)

print(dir(tuple))

# Main tuple methods:

# T.count()
# T.index()

# Since tuples cannot be modified,
# modification methods are not provided.


# 6. ERROR PRONE
#------------------------------------------------------------------

# Lists are more error-prone because values can change accidentally.

L = [1, 2, 3]

L[0] = 999

# Data changed accidentally.

# Tuples are safer because data cannot be modified.

T = (1, 2, 3)

# T[0] = 999
# Error raised immediately

# Therefore tuples are useful when data should remain constant.


# 7. USABILITY
#------------------------------------------------------------------

# Use Lists when data will change frequently.

shopping_cart = ["Milk", "Bread", "Eggs"]

shopping_cart.append("Butter")

# Use Tuples when data should remain fixed.

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

# Days of the week should not change,
# so Tuple is a better choice.


# INTERVIEW SUMMARY
#------------------------------------------------------------------

# LIST
# Mutable
# Slower
# More Memory
# More Methods
# Better for frequently changing data

# TUPLE
# Immutable
# Faster
# Less Memory
# Fewer Methods
# Better for fixed data


#Difference in speed
import time

L = list(range(10000000))
T = tuple(range(10000000))

start = time.perf_counter()

total = 0
for i in L:
    total += i * 5

print("List Time :", time.perf_counter() - start) #Output: List Time : 0.6268239000346512

start = time.perf_counter()

total = 0
for i in T:
    total += i * 5

print("Tuple Time:", time.perf_counter() - start) #Output: Tuple: 0.6035076000262052


#Difference in Memory

import sys

LI = list(range(1000))
TU = tuple(range(1000))

print('List size',sys.getsizeof(LI)) #Output: List size 8056 From the module sys we use the function getsizeof to find out the memory size consumed
print('Tuple size',sys.getsizeof(TU)) #Output: Tuple size 8040

#Prone to Error

#Error in list

a = [1, 2, 3]
b = a

a.append(4)

print(a) #Output: [1, 2, 3, 4]
print(b) #Output copied to b as well -> [1, 2, 3, 4]

#Same error is not in Tuple

c = (1, 2, 3)
d=c

c = c + (4,) #tuples are immutable so this is the only method

print(c) #output: (1, 2, 3, 4)
print(d) #output: (1, 2, 3)


#SPECIAL SYNTAX

#1. Tuple Unpacking: If we want we can unpack the values of a tuple and save it inside a variable.

a, b, c = (1, 2, 3)

print(a) #output: 1

print(a, b, c) #output: 1 2  3

#Using tuple unpacking to swap values

a = 1
b = 2
a,b = b,a

print(a, b) #output: 2 1

#In a scenario where where we only require a fixed value, say first two value

a, b, *others = (1, 2, 3, 4)

print(a, b) #Output: 1 2

print(others) #outputs list of remaining items [3, 4]

#2. ZIPPING TUPLES: It operates on per item iterables for atleat two . it creates a zip object. to chek zip object
# we can either conver to list or tuple

a = (1, 2, 3, 4)
b = (5, 6, 7, 8)

zip(a,b) #outputs <zip object at 0x00000230E9BCF140>

list(zip(a,b)) #outputs [(1, 5), (2, 6), (3, 7), (4, 8)] -> List of Tuples

tuple(zip(a,b)) #outputs ((1, 5), (2, 6), (3, 7), (4, 8))

################################################################################################################################

#