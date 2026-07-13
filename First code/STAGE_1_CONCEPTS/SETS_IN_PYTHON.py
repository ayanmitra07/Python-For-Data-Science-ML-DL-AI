#----------------------------------------------------------------------
#SECTION 17: SETS IN PYTHON (PART 1)
#----------------------------------------------------------------------

#A set is an unordered collection of items. Every set element is unique (no duplicates) and must be 
# immutable (cannot be changed).

#However, a set itself is mutable. We can add or remove items from it.

#Sets can also be used to perform mathematical set operations like union, intersection,
#  symmetric difference, etc.

#Characterstics:

#Unordered
#Mutable
#No Duplicates
#Can't contain mutable data types

#Plan of attack
#1. Creating a Set
#2. Accessing items in set (error)
#3. Editing items in set(error)
#4. Adding items in set
#5. Deleting items in sets
#6. SET Operation
#7. Set Functions
#8. Frozenset
#9. Set comprehension

#1. Creating a Set
#-----------------------------------------------------
#empty set

s = set()
se = {}

print(type(s)) #<class 'set'>
print(type(se)) #<class 'dict'>


#1D and 2D

s1 = {1, 2, 3}
print(s1) #Outputs: Homogenious set-> {1, 2, 3}

s2 ={1, 2, 3, {4, 5}}

print(s2) #Outputs TypeError: unhashable type: 'set'. We cannot have a mutable(changing) datatype inside a set

#Hetrogeneous set

s3 = {1, 'Hello', 4.5, True}

print(s3) #Outputs: {1, 4.5, 'Hello'} # we do not see True because in python True =1 and python set cannot have duplicates

s4 = {2, 'Hello', 6.5, True}

print(s4) #Outputs:{True, 2, 'Hello', 6.5}

#we can add tuple because it is immutable

s5 = {1, 'Hello', 4.5, True,(1, 2, 4)}

print(s5) #Output: {1, 'Hello', 4.5, (1, 2, 4)}

#the output is not in the order we provided because sets do not honour order. They are unordered.
#internally an algorithm is running which is called hashing. Hashing decide what items will sit where.

#Sets using Type Conversion

s6 = set(['G',0, 'A', 'T'])

print(s6) #Output: {'G', 0, 'A', 'T'}

#Duplicates are not allowed in sets

s7 = {1, 1, 2, 2, 3, 3, 3}

print(s7) #Outcome: {1, 2, 3}

#Sets are unordered

s1 = {1, 2, 3}

s2 = {3, 2, 1}

s3 = {1, 2, 3}

print(s1 == s2) #output: TRUE. Beause the order does not matter

print(s1 == s3) #output: TRUE

#ACCESSING ITEMS IN SET
#----------------------------------------------------------------------------

#using indexing we will not be able to acces items in set

s1 = {1, 2, 3, 4}

s1[0] #Output: TypeError: 'set' object is not subscriptable. This implies sets are unordered and
                # does not follow the concept of indexing(Positive or negative)

s1[0:4] #Output: TypeError: 'set' object is not subscriptable. Slicing is also not possible

#Once an item is inside set. changes cannot be made. Therefore accessing items does not work since
# it is unordered]

#EDITING ITEMS IN SET
#-----------------------------------------------------------------------------------

s1 = {1, 2, 3, 4}

s1[0] = 100 # Output: 'set' object does not support item assignment. this is because indexing does not work.

#ADDING ITEMS IN SET
#-----------------------------------------------------------------------------------

#We can add items within set
 
#1. add(): Provide the feature of adding a single item
 
S = {2, 4, 8, 16}

S.add(32)

print(S) #Outputs: {32, 2, 4, 8, 16}. Add function adds a single item wherever the Hash algorithm wants the index postion to be.

#2. update(): Provides us the feature to update with multiple items

S.update([1,3,5,6,7, False , 'GTA IV'])

print(S) #Outputs: {32, 1, 2, 3, 4, 5, 6, 7, 8, False, 16, 'GTA IV'}


#DELETING ITEMS IN SET
#----------------------------------------------------------------------------------------

#1. del: Deletes entire set
sd = {2, True, 'FOX KIDS'}

print(sd) # Output: {True, 2, 'FOX KIDS'}

del sd

print(sd) #Outputs: NameError: name 'sd' is not defined. the whole set is deleted

sod = {1, False, 'Swat Cats'}

print(sod) #Outputs: {False, 1, 'Swat Cats'}
del sod[1] #Output: TypeError: 'set' object doesn't support item deletion. Since indexing does not work in set,
            #we cnnot delete any particular item

#2. discard(): With the help of discard we can tell which item we want to be deleted.
            #it will not provide error if you discard an item not present in the set.

sod.discard('Swat Cats')

print(sod) #Outputs: {False, 1}

#3. remove(): With the help of remove we can tell which item we want to be deleted.
            #it will provide error if you discard an item not present in the set.


r = {1,2, 4, 7.5}
r.remove('Swat Cats') #output: KeyError: 'Swat Cats'

#4. pop() randomly deletes an item

r.pop() #output: randmly deleted 1

print(r) #output: {2, 4, 7.5}

#5. clear empties the entire set and leaves behind an empty set

r. clear()

print(r) #output: set()


#OPERATIONS IN SETS
#---------------------------------------------------------------------------------------------

#1. UNION(|): Combines the sets

s1 = {1, 3, 3, 5, 2}
s2 = {2, 4, 4, 6, 5}

uni = s1|s2

print(uni) #output: {1, 2, 3, 4, 5, 6}. No duplicates will be kept.

#2. Intersection (&): Only keeps the common item from both the set

inter = s1&s2

print(inter) #output: {2, 5}

#3. Difference (-)

diff = s1 - s2 
print(diff) #output: {1, 3}. Items from s1 not present in s2

diff2 = s2 - s1

print(diff2) #output: {4, 6}. Items from s2 not present in s1

#4. Symmetric differencr (^) provides all items except the common items.

sydiff = s1 ^ s2

print(sydiff) #output: {1, 3, 4, 6}

#5. Membership test(In and Not IN)

1 in s1 #output: True

1 not in s1 #output: False

#6. Iteration

for i in s1:
    print(i) #output:#1
                    #2
                    #3
                    #5

# SET FUNCTION

#BUILT IN FUNCTION: 

#1. len()

s = {2, 5, 7, 5, 1, 9, 0}

len(s) #Output: 6. Duplicates are not considered

#2. sum()

sum(s) #Output 24. Duplicates are not considered

#3. max()

max(s) #Output 9

#4. min()

min(s) #output 0

#5. Sorted(): the result of sorted will always come in a list

sorted(s) #Output: [0, 1, 2, 5, 7, 9]

sorted(s,reverse = True) #Output: [9, 7, 5, 2, 1, 0] this is in descending order

#--------------------------

#Other function

#Union() and update(): This function is same as using the operator UNION(|)

s1 = {'Mat', 4, 2.5}
s2 = {1,2,'Cat', False}

s1.union(s2) #Output: {False, 1, 2.5, 2, 4, 'Cat', 'Mat'}

print(s1) #output is still {2.5, 'Mat', 4}

print(s2) #output is still {False, 1, 2, 'Cat'}

#update()

s1.update(s2)

print(s1) #output is now updated to {False, 1, 2.5, 2, 4, 'Cat', 'Mat'} as it was in union but permanent changes

print(s2) #output is still {False, 1, 2, 'Cat'}

#-------------------------

#intersection() and intersection_update()

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s1.intersection(s2) #output: {4, 5}

print(s1) #output s1 still remains {1, 2, 3, 4, 5}

s1.intersection_update(s2)

print(s1) #output s1 now becomes and stays {4, 5}

#---------------------------

#difference/difference_update

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s1.difference(s2) #Outcome: {1, 2, 3}

print(s1) #Outcome remains same: {1, 2, 3, 4, 5}

s1.difference_update(s2)

print(s1) #Outcome changes to and stays {1, 2, 3}

#----------------------------

#symmetric_difference/symmetric_difference_update()
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s1.symmetric_difference(s2) #Outcome: {1, 2, 3, 6, 7, 8}

print(s1) #Outcome remains same: {1, 2, 3, 4, 5}

s1.symmetric_difference_update(s2)

print(s1) #Outcome changes to and stays {1, 2, 3, 6, 7, 8}

#----------------------------

#isdisjoint: Suppose we have two sets, with the help of disjoint we find out if there are no common items between them.

s1 = {1, 2, 3, 4}
s2 = {5, 6, 7, 8}

s1.isdisjoint(s2) #Output: True

#issubset: if the items of the second set are already present in the intial set


s1 = {1, 2, 3, 4, 5, 6}

s2 = {2, 3, 7}

s3 = {4, 5, 6}

s1.issubset(s2) #output: False, since s1 is not a subset of s2

s2.issubset(s1) #output: False since s2 contains 7 whioch is not in s1

s3.issubset(s1) #output: True since all the items in s3 are already with s1

#issuperset

s1.issuperset(s2) #output: False, since s1 is not a superset of s2


s1.issuperset(s3) #output: True since all the items in s3 are already with s1

#copy: Creates a shallow copy

s1 = {1, 2, 3}

s2 = s1.copy

print(s1)
print(s2)

#FROZENSET: This is an immutable version of python set object. that is once it is created nothing can be added
#or deleted
#--------------------------------------------------------------------------------/

#Create frozen set

fs = frozenset([1, 2, 3])

print(fs) #Output: frozenset({1, 2, 3})
print(type(fs)) #Output: <class 'frozenset'>

#when using frozen set all the operation and function pefrormed in set will also work on frozen set since
#all this operation does not do any changes in set we are just reading the values.
#but function like add and delete only works on set but frozenset will not change

fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])

#union

fs1|fs2 #output: frozenset({1, 2, 3, 4, 5})

#2D frozen set is also possible

fs3 = frozenset([ 1, 2, frozenset([3, 4])])

print(fs3) #output: frozenset({frozenset({3, 4}), 1, 2})

#SET COMPREHENSION
#-----------------------------------------------------------------

{i for i in  range(1, 10)} # output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

{i for i in range(1,11) if i >5} #Output {6, 7, 8, 9, 10}

{i**2 for i in range (1, 11) if i>6} #Output {64, 49, 100, 81}


