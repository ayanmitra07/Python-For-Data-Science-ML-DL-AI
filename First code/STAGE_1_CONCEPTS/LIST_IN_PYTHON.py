#----------------------------------------------------------------------
#SECTION 15: LIST IN PYTHON (PART 1)
#----------------------------------------------------------------------

#Q1. What is a List?
#Q2. Difference between List and Array?
#Q3. How to create a List
#Q4. How to Access a list
#Q5. How to edit a list
#Q6. How to add a list
#Q7. How to delete a list
#Q8. Operations in list
#Q9. Functions in list


# A list is a datatype where we can store multiple things.

# Although array and list are fundamentally are same
#but few of the difference is 
# 1. Array is homogenious, so same datatype. 
# List on the other hand can have different types of datatype as a result it can be hetrogenious.

#2. Array is stored continiousluy on the memory. 
# This is not necessary in list. In list it is not 
# stored one after the other. As a result arrays are much faster and takes less memory compared to list.

#3. Arrays are of fixed size,in other words before using Array we need to declare 
# how many items we are going to store. Where as we do not have to mention the 
# no. of items we are going to store in list, we can add items on the go there is no limit and hence flexible.

#4. List are more programmer friendly, but it has a disadvantage that is it is slow. 
# But programmers builds logic more effectively on list in comparison to arrays

#Creating an empty list

L1 = []

print(L1)

#Creating Heterogenious list

L2 = [1, "Hello", True, 5+6, 7.9]

print(L2)

#Multidimensional List 

#2D list

L3 = [1,2,3,[4,5]]

print(L3)

#3D List

L4 = [[[1,2], [3,4]],[[5,6] , [7,8]]]

print(L4)

#List through type conversion

L5 = list("KASHMIR")

print(L5) #Output: ['K', 'A', 'S', 'H', 'M', 'I', 'R']

L6 = list()

print(L6) #Outputs: Empty List []

# ACCESSING ELEMENTS IN PYTHONG
#---------------------------------------------

#INDEXIN-----------------------------------------------------------------------
L7 = [1, 2, 3, 4]

print(L7[0]) #Positive Indexing outputs 1 the first postion of the list L1

print(L7[-1]) #Negative Indexing outputs 4 the first postion of the list L1

#Incase of a 2D list Indexing will work like below

List2D = [1, 2, 3, [4, 5]]

print(List2D[-1]) #Indexing outputs the entire nested list containing [4, 5]

print(List2D[-1][-2]) #Negative Indexing outputs the second last element of the nested list which is 4

print(List2D[3][0]) #Positive Indexing outputs the second last element of the nested list which is 4

#Nested Indexing for 3D list

List3D = [[[1, 2] ,[3, 4]], [[5, 6] ,[7, 8]]]

print(List3D[0]) #Postive indexing for the list at first postion [[1, 2], [3, 4]]. This output result in 2D list

print(List3D[1][0]) #Postive indexing -> [1] for the list at second postion [[5, 6], [7, 4]]. Then wrt [0] it provides the list [5, 6] as output

print(List3D[1][0][0]) #positive indexing resulting in 5

#Slicing ------------------------------------------------------------------------
#When we want to extract multiple items together from a list we use slicing

SLI7 = [1, 2, 3, 4, 5, 6, 7]

print(SLI7[1:3]) #Outputs [2, 3]

print(SLI7[-3:]) #outputs the last three items

print(SLI7[-3:-1]) #outputs after -3 except the last item

print(SLI7[0::2]) #outputs alternate items [1, 3, 5, 7].here the 2 acts as the number of items we jump

print(SLI7[-5:-2]) #outputs [3, 4, 5]

print(SLI7[-5:-2 :2]) #outputs [3, 5]

print(SLI7[::-1])# Outputs the reverse list [7, 6, 5, 4, 3, 2, 1]

L3 = [1,2,3,[4,5]]

#ADDING ITEMS TO A LIST
#--------------------------------------------
#There are three ways too add items to a list

#Append-----------------
#If we use append then we can only append one item at a time to a list at the end

App = [1, 2, 3, 4, 5]

App.append(6)
print(App) #Outputs: [1, 2, 3, 4, 5, 6]

#appending a list

applst = [1, 2, 3, 4, 5]

applst.append([6, "Hello", False])

print(applst) # Outputs a nested list where it adds the new list as a single item

#Extend-----------------
#If we use extend we can add multiple item to an exisiting list

ext = [1, 2, 3, 4, 5]

ext.extend([6, 7, "Hello", True, 9.77])

print(ext) # Outputs [1, 2, 3, 4, 5, 6, 7, 'Hello', True, 9.77]

#Extending on a sing item

ext1 = [1, 2, 3, 4, 5]

ext1.extend('Delhi')

print(ext1) #outputs: [1, 2, 3, 4, 5, 'D', 'e', 'l', 'h', 'i']. so each letter it treast as a single item and 
            #adds them as individual elements

#Insert allows us to add at a desired location -------------------------
#we provide the index postion and the item we want to insert after it. 
#We cannot add multiple items using insert

#for example we will insert between 1 and 2
ins = [1, 2, 3, 4, 5]

ins.insert(1, 100)

print(ins)

#Editing exixting item in a list
#----------------------------------------------------------------------

#Changing existing items in a list-------------

exch = [1, 2, 3, 7, 5]

exch[-1] = 500 #Editing using indexing

print(exch) #output: [1, 2, 3, 7, 500]

exch[1:4] = [200, 300, 400] #Editing using slicing

print(exch) #Output: [1, 200, 300, 400, 5]

#Deleting items from a list-------------
#we use del, remove, pop and clear

#del------

cln = [1, 2, 3, 4, 5]

print(cln)

del cln

print(cln) #Output: cln does not exist. But as per the memory level it is still not deleted.

del cln[-1] #deleting through indexing

print(cln) #Output: [1, 2, 3, 4]

del cln[1:3] #deleting through slicing

print(cln)# doesn't iclude the last item so output [1, 4, 5]

#remove--------
#it removes an item as per the value

rem = [1, 2, 3, 4, 5]

rem.remove(5) # removes the valu 5 from the [1, 2, 3, 4]

print(rem)

#pop---------
#it can deleteing an item at a particular index

pp = ["SOL", 5, 7, True]

print(pp.pop(0)) # deletes 0th index "SOL"

print(pp) #output: [5, 7, True]

#if we do not provide an index the last item will be deleted

print(pp.pop()) #deletes the item True

print(pp) # Output: ['SOL', 5, 7]

#clear--------
#it clears all the item within a list and makes it an empty list

clr = [ "TMNT", "Ninja Robots", "Transformers", "Centurions"]

clr.clear()

print(clr) #outputs an empty list -> []

#OPERATIONS ON LIST (Arithmetic, Membership and Loop)
#----------------------------------------------

#Arithmetic(+, *)---------

#Adding two list results in concatination/Merge

a1 = [2, 4, 6]

b2 = [1, 3, 7]

print(a1 + b2) #Output: [2, 4, 6, 1, 3, 7]

#Multiplication results in repeating and then merging

print(a1*3) # Outputs: [2, 4, 6, 2, 4, 6, 2, 4, 6]

#Membership (IN, NOT IN)

a2 = [1, 2, 3, 4, 5]

b3 = [1, 2, 3, 4, [5, 6,]]

print( 5 in a2) #Outputs True

print( 5 not in a2) #Outputs False

print (5 in b3) #Outputs False, 5 is not under the main list

print ([5, 6] in b3) #Outputs True because the list [5, 3] is present within the main list

#loops using operation
#loops work on sequence and list is a sequence

a2 = [1, 2, 3, 4, 5]

b3 = [1, 2, 3, 4, [5, 6,]]

for i in a2:
    print(i) #outputs: 1, 2, 3, 4, 5

for i in b3:
    print(i) #outputs: 1, 2, 3, 4, [5, 6

c3 = [[[1,2], [3,4]],[[5,6], [7,8]]]

for i in c3:
    print(i) 
    # itereates only twice ->c3 =First element: [[1, 2], [3, 4]] and Second element: [[5, 6], [7, 8]]
    #do this in terminal instead first for i in c3: then on the next line     print(i), after that onemore enter

#FUNCTIONS IN LIST
#---------------------------------------------------------------------

#Universal function found in list, string, sets, tuples, dictionary
#len, min, max, sorted

dis = [2, 6, 8, 0, 5, 1]

print(len(dis)) #output: 6 #len function counts the number of items in a list

print(min(dis)) # output: 0. Only works when list is homogenious data values. min function provides the minimum value

print(max(dis)) #output: 8

print(sorted(dis)) #output: [0, 1, 2, 5, 6, 8]

print(sorted(dis, reverse = True)) #output: [8, 6, 5, 2, 1, 0]

#Count--------------
#provides the frequency count of an item

dup = [2, 6, 8, 0, 5, 1, 3 ,5 , 2, 4, 7, 2]

print(dup.count(2)) #Output 3

#Index--------------
#Provides the index postion of an item

print(dup.index(5)) #output: 4 . postion of the item's first occurence

#reverse-------------
#permanenty reverses the list

rev = [1,2, 3]

rev.reverse()
print(rev) #outputs [3, 2, 1]

#sort-------(Sort Vs Sorted)
#just like sorted the sort function orders as per some rule 
# but the affect is permanent unlike sorted where affect is temporary

ju = [2, 4, 6, 8, 1, 3, 5]

print(ju) #[2, 4, 6, 8, 1, 3, 5]
print(sorted(ju)) # [1, 2, 3, 4, 5, 6, 8]
print(ju)# [2, 4, 6, 8, 1, 3, 5], Temporary changes does not affect the original value

ju.sort()
print(ju)# [1, 2, 3, 4, 5, 6, 8]. Permanent changes to original value

#copy----------------
#creates a copy of the list in the memory. but it stores at different id address
#values are same but list are different
#copy creates a shallow copy
#study deep copy Vs Shallow copy

add1 = [1, 7, 8, 2]

print(add1)
print(id(add1)) #MEMORY ADDERESS: 1498332897664

add22 = add1.copy()

print(add22)
print(id(add22)) #MEMORY ADDERESS: 1498332897600


# Memory address of elements in list using id()
#---------------------------------------------

a = 2

print(id(a)) #Memory address using id() -> 140735823311688
print(id(2)) #Memory address using id() -> 140735823311688

L = [1, 2, 3] # searching the memory address of a list

print(id(L)) #Memory address of entire list using id() -> 2160997952384
print(id(L[0])) #Memory address of index element 0 of list using id() -> 140735823311656
print(id(L[1])) #Memory address of index element 1 of list using id() -> 140735823311688
print(id(L[2])) #Memory address of index element 2 of list using id() -> 140735823311720

print(id(1)) #Memory address of element 1 of list using id() -> 140735823311656
print(id(2)) #Memory address of element 2 of list using id() -> 140735823311688
print(id(3)) #Memory address of element 3 of list using id() -> 140735823311720

#As per the output from above the address for the list as well as address of each 
# elemnets with list all are different.
#However the index element will provide the same memory address as the elemnt in question. 
#this is because the memory address, say 140735823311656 which is the memory address of the postion L[0]
# which is actually 1 as  a result it is showing the same memory address.

# The concept of dynamic array is we start with a fixed size array and then add items. once the array reaches a limit
#we create a new array and continue which is double the size of the previous array and so on.

#Characteristics of a List
#------------------------------------

#1. Ordered: the order of the elements in the list is important. For example the below list are not same:

L = [1, 2, 3]

L1 = [3, 2, 1]

L == L1 # output: False

#Although the elements in a list are same but the ordering is not same.

#2. Changable/Mutable

#Python List is a mutable datatype. so we can change the value at a certain position
#  which was already occupied earlier. Python list is dynamic array

#3. Heterogenious

# we can add multiple different types of datatypes in a list


L2 = [1, "Hello", True, 5+6, 7.9]

#4. Can have duplicates

# list canhave duplicate items

L21 = [1, 2, 4, 1]

#4.  Dynamic

# list are dynamic this means as we keep increasing items with a list, 
# it will keep on increasing the memory by itself

#5. List can be Nested

#we can put a list with another list

#6. Items with a list can be accessed

#using indexing or slicing we can extract items from a list

#7. List can contain any kind  of objects in Python


#LIST COMPREHENSION
#---------------------------------------------------------------

#newlist = [expression for item in iterable if condition == True]

#Advantage of list Comprehension
#More rime-efficient and space-efficient than loops
#Require fewer lines of code
#Transforms iterative statement into formula

#Add 1 to 10 members to a list using normal python code

L= [] #Create empty list to append sata from loop

for i in range(1,11):
    L.append(i)

print(L)

#Add 1 to 10 members to a list using list comprehension

L2 = [i for i in range (1,11)]

print(L2)

#scalar multiplication on a vector using normal python code

v = [2, 3, 4]

s = -3
m = 3

print(v*s) # returns empty list a negative scalar doesnt work
print(v*m) # returns [2, 3, 4, 2, 3, 4, 2, 3, 4]

#using loop

x = []

for i in v:
    x.append(i*s)

print(x) #Outputs: [-6, -9, -12]

#Alternatively doing scalar multiplication on a vector using list comprehension

[s*i for i in v] #Outputs: [-6, -9, -12]

#Adding squares using list comprehension

N = [2, 4, 5, 7]

[i**2 for i in N] # Outputs [4, 16, 25, 49]

#we can use if condition with the list comprehension as well in addition to loop

# Print all numbers divisible by 5 in range of 1 to 50

vd = [i for i in range (1,51) if i%5==0]

print(vd) #Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

#Find languages starting with p

languages = ['jave', 'python', 'php', 'c', 'javascript']

[lang for lang in languages if lang.startswith('p')] #output: ['python', 'php']

#Nested if with List Comprehension

basket = ['apple', 'guava', 'cherry', 'banana']
my_fruit = ['apple', 'kiwi', 'grapes', 'banana']

#add new list from my_fruits and items if the fruit exist in basket and also starts with 'a'

[fruit for fruit in my_fruit if fruit in basket if fruit.startswith('a')] #output: ['apple']

# Print a (3,3) matrix using list comprehension ->Nested list comprehension

[[i*j for i in range (1,4)] for j in range (1,4)] #outputs 2d list of 3X3 Matrix [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Cartesian products -> List comprehension on 2 list together

L1 = [1 , 2, 3, 4]
L2 = [5 , 6, 7, 8]

[i*j for i in L1 for j in L2] #Outputs: [5, 6, 7, 8, 10, 12, 14, 16, 15, 18, 21, 24, 20, 24, 28, 32]

#TWO WAYS TO TRANSVERSE A LIST
#itemwise
#Indexwise

#1. Itemwise

L = [1, 2, 3, 4]

for i in L:
    print(i) #outputs the list

#2. Indexwise

for i in range (0,len(L)): # length of the list L provides index of the item
    print(i) #outputs index position of list 0 1 2 3


for i in range (0,len(L)): # length of the list L provides index of the item
    print(L[i]) #Outputs 1 2 3 4


