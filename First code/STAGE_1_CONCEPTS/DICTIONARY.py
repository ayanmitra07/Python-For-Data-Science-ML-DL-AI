#----------------------------------------------------------------------
#SECTION 18: DICTIONARY IN PYTHON
#----------------------------------------------------------------------

#Dictionary
#Dictionary in Python is a collection of keys values, used to store data values like a map, 
# which, unlike other data types which hold only a single value as an element.

#In some languages it is known as map or assosiative arrays.

#dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

#Characterstics:

#Mutable
#Indexing has no meaning
#keys can't be duplicated
#keys can't be mutable items
#unordered

#PLAN OF ACTION
#------------------
# create a dictionary
# accessing items
# adding key-value pair
#remove key-value pair
#editing key-value pair
#dictionary operations
# dictionary functions
#dictionary comprehension
#zip()
#nested comprehension
#doubt clearance & Session end

#--------------------------------------------------------------

#CREATING A DICTIONARY
#----------------------------------------------------

#1. EMPTY Dictionary

d = {}

print(type(d)) #Output: <class 'dict'>
print(d) #Output: {}

#2. 1D Dictionary (Homogeneous)

d1 = {'name':'Ayan Mitra', 'gender':'Male'}

print(d1) #output: {'name': 'Ayan Mitra', 'gender': 'Male'}

#3. With mixed key (here we use tuple and string which are both immutable)

d2 = {(1, 2, 3): 1, 'Name': 'Ayan'}

print(d2) #Outlook: {(1, 2, 3): 1, 'Name': 'Ayan'}

#4. Nested Dictionary(JSON follows this kind of format)

d4 = {
    'Name': 'Ayan',
    'Gender':'Male',
    'SEM': 3,
    'Subjects':{'Maths': 48, 'Economics': 49, 'Statistics': 50}
}

print(d4) #Outlook: {'Name': 'Ayan', 'Gender': 'Male', 
                    #'SEM': 3, 'Subjects': {'Maths': 48, 'Economics': 49, 'Statistics': 50}}

#5. Dictionary using dict function and sequence
#we pass a list of tuples which automaticcaly forms a dictionary after using the dict function.

d5 = dict([('Name', 'Ayan'), ('Age', '22'), (4,'Four')])

print(d5) #Output: {'Name': 'Ayan', 'Age': '22', 4: 'Four'}

#6. Duplicate keys are not allowed

d6 = {'Name': 'Ayan', 'name': 'Rohit'} #Output: Keys are case sensitive

print(d6)

d7 = {'Name': 'Ayan', 'Name': 'Rohit'}

print(d7) #output: {'Name': 'Rohit'} ->Takes the last known key value pair

#7. Mutable items as keys are not allowed

d8 = {'name': 'Ayan',
      [1,2,3]: 'These are list items'}

print(d8) #outlook: TypeError: unhashable type: 'list'. since [1 , 2, 3] is a list which is mutable and cannot be used as a key

d9 = {'title': 'Mitra',
      (1, 2, 3): 'This is a tuple'} #outlook: {'title': 'Mitra', (1, 2, 3): 'This is a tuple'}

print(d9) #outlook: {'title': 'Mitra', (1, 2, 3): 'This is a tuple'}. (1, 2, 3) is a tuple and thus immutable

#------------------------------------------------------------------------------------------------------------

#ACCESSING ITEMS FROM A DICTIONARY
#--------------------------------------------------------------------------
#indexing does not work in dictionary

my_dict = {'Name': 'Ayan', 'Gender': 'Male'}

print(my_dict[0]) #output: error

#we need to provide the key

my_dict['Name'] #Output 'Ayan'

#Using get() we can obtain the velue

my_dict.get('Gender') #Output 'Male'

#Accessing from 2D dictionary
#we will first fetch the inner dictionary that is Subject for us

s = {
    'Name': 'Ayan',
    'Gender':'Male',
    'SEM': 3,
    'Subjects':{'Maths': 48, 'Economics': 49, 'Statistics': 50}
}

s['Subjects'] #outlook: {'Maths': 48, 'Economics': 49, 'Statistics': 50}

#if we want a particular value from the 2D dictionary

s['Subjects']['Maths'] #outlook: 48

#ADDING KEY-VALUE PAIR
#---------------------------------------------------------------------------------------

d6 = {'Name': 'Ayan', 'name': 'Rohit'}

d6['gender'] = 'male'

print(d6)

d6['weight'] = 75

print(d6) #output: {'Name': 'Ayan', 'name': 'Rohit', 'gender': 'male', 'weight': 75}

#adding a new key value pair in 2d dictionary
s = {
    'Name': 'Ayan',
    'Gender':'Male',
    'SEM': 3,
    'Subjects':{'Maths': 48, 'Economics': 49, 'Statistics': 50}
}

s['Subjects']['Data Science'] = 50

print(s) #outcome: {'Name': 'Ayan', 'Gender': 'Male', 'SEM': 3, 
                        #'Subjects': {'Maths': 48, 'Economics': 49, 'Statistics': 50, 'Data Science': 50}}


#REMOVE KEY VALUE PAIR
#--------------------------------------------------------------------------------------

#1. pop: Removes the key value pair if we mention which key to remove

d7 = {'Name': 'Ayan', 'name': 'Rohit', 'gender': 'male', 'weight': 75}

d7.pop('name') #output: removes 'Rohit'

print(d7) #output: {'Name': 'Ayan', 'gender': 'male', 'weight': 75}

#2.popitem(): Deletes the last item pair of the dictionary

d7.popitem() #output: removes ('weight', 75)

print(d7) #output: {'Name': 'Ayan', 'gender': 'male'}

#3. del: Removes the entire dictionary and if we want we can delete specific key value pair.

#specific  key value pair with del

del d7['Name']

print(d7) #Output: {'gender': 'male'}.

#it can delete the entire dictionary

del d7

print(d7) #outlook NameError: name 'd7' is not defined.

#Removing a key value pair in 2d dictionary
s = {
    'Name': 'Ayan',
    'Gender':'Male',
    'SEM': 3,
    'Subjects':{'Maths': 48, 'Economics': 49, 'Statistics': 50, 'Data Science': 50}
}

del s['Subjects']['Data Science']
print(s) #deletes one specified key value pair at a time.

#4. clear : Empties the entire dictionary

d8 = {'Name': 'Ayan', 'Console wishlist': 'PS5 pro', 'gender': 'male', 'weight': 75}

d8.clear()

print(d8) #Output: {}


#EDITING KEY_VALUE PAIR
s = {
    'Name': 'Ayan',
    'Gender':'Male',
    'SEM': 3,
    'Subjects':{'Maths': 48, 'Economics': 49, 'Statistics': 50, 'Data Science': 50}
}

s['SEM'] = 4

print(s) #output: {'Name': 'Ayan', 'Gender': 'Male', 'SEM': 4, 
                        #'Subjects': {'Maths': 48, 'Economics': 49, 'Statistics': 50, 'Data Science': 50}}

s['Subjects']['Statistics'] = 45

print(s) #Output: {'Name': 'Ayan', 'Gender': 'Male', 'SEM': 4,
                  #'Subjects': {'Maths': 48, 'Economics': 49, 'Statistics': 45, 'Data Science': 50}}

#DICTIONARY OPERATIONS
#-------------------------------------------------------------------

#Membership
#Iteration

s = {
    'Name': 'Ayan',
    'Gender':'Male',
    'SEM': 3,
    'Subjects':{'Maths': 48, 'Economics': 49, 'Statistics': 50, 'Data Science': 50}
}

print (s) #{'Name': 'Ayan', 'Gender': 'Male', 'SEM': 4, 
            #'Subjects': {'Maths': 48, 'Economics': 49, 'Statistics': 45, 'Data Science': 50}}


#Membership operator works on keys only
'Ayan' in s #output: False
'Name' in s #output: True

#iteration through loop

d = {'Name': 'Ayan','Gender':'Male','SEM': 3,'Subjects':{'Maths': 48, 'Economics': 49, 'Statistics': 50, 'Data Science': 50}}

for i in d:
    print(i) #prints the Keys ->Name | Gender | SEM |Subjects

for i in d:
    print(i,d[i]) #outputs: 'Name': 'Ayan' | Gender Male | SEM 3 | Subjects Maths

#iteration in 2D dictionary

# .items() returns both the key and value together.
# Example:
# ('Name', 'Ayan')
# ('Gender', 'Male')
# ('SEM', 3)
# ('Subjects', {...})

for key,value in d.items():
    #Checks if th current value is dictionary, if yes it is a nested dictionary
    if isinstance(value,dict):

        print(key) #print the outer key

        #at this point within the instance the value here will be a dictionary
        # we use another loop
        for sub_key,sub_value in value.items():
            print(" ",sub_key,":", sub_value)
    else:
        # If the value is NOT a dictionary
        # (it may be a string, integer, float, list, etc.)
        # simply print the key and its value.
        print(key, ":", value)

#Output:Name : Ayan
#Gender : Male
#SEM : 3
#Subjects
  #Maths : 48
  #Economics : 49
  #Statistics : 50
  #Data Science : 50

#--------------------------------------------------------------------------------------------------------

#DICTIONARY FUNCTION
#---------------------------------------------

#1. len()

len(d) #output 4(outer key values)

#2.Sorted()

sorted(d) #output: ['Gender', 'Name', 'SEM', 'Subjects']

sorted(d, reverse =True) #Output: ['Subjects', 'SEM', 'Name', 'Gender']

#3. min and max

min(d) #Output: 'Gender' based on ASCII value

max(d) #output:v'Subjects'

#4. items(): provides all the key value pair in the form of tuples

print(d.items()) #output: dict_items([('Name', 'Ayan'), ('Gender', 'Male'), ('SEM', 3), 
                    #('Subjects', {'Maths': 48, 'Economics': 49, 'Statistics': 50, 'Data Science': 50})])

#5. keys: prints all the keys within first dictionary

print(d.keys()) #output: dict_keys(['Name', 'Gender', 'SEM', 'Subjects'])


#6. Values: prints all the values within a the first dictionary

print(d.values()) #output: dict_values(['Ayan', 'Male', 3, 
                    #{'Maths': 48, 'Economics': 49, 'Statistics': 50, 'Data Science': 50}])

#7. update: 

d1 = {'one': 1, 'Three': 3, 'Five': 5, 'Seven': 7, 'Nine': 9}

d2 = {'Two': 2, "Four": 4, 'Seven': 8}

d1.update(d2)

print(d1) #Output:{'one': 1, 'Three': 3, 'Five': 5, 'Seven': 8, 'Nine': 9, 'Two': 2, 'Four': 4}. 
#the values not only got appended but changed as well if you notice seven

#--------------------------------------------------------------------------------------------------------

#DICTIONARY COMPREHENSION
#{key:value for vars in iterable}

# 1. Print 1st 10 number comprehension and their squares

{i:i**2 for i in range(1,11)} #output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

#2. using existing dict

distances = {'delhi':1000,'mumbai':2000,'bangalore':3000}

print(distances.items()) #output: dict_items([('delhi', 1000), ('mumbai', 2000), ('bangalore', 3000)])

{key:values*0.65 for key,values in distances.items()} #output:{'delhi': 650.0, 'mumbai': 1300.0, 'bangalore': 1950.0}

#3. Dictionary comprehension using zip(). we will use two lsit to make one dictionary

# zip() combines multiple iterables (lists, tuples, strings, etc.)
# element-by-element into a single iterator of tuples.
# The first element of each iterable is grouped together,
# then the second element, then the third, and so on.

# Syntax:
# zip(iterable1, iterable2, ...)
# It stops when the shortest iterable is exhausted.

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

temp1= [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

{key:value for (key,value) in zip(days,temp1)}

#output{'Sunday': 30.5, 'Monday': 32.6, 'Tuesday': 31.8,
#  'Wednesday': 33.4, 'Thursday': 29.8, 'Friday': 30.2, 'Saturday': 29.9}

#dictionary comprehension with if condition

#create a new dictionay without items whose stock is zero

products = {'phone':10,'laptop':0,'charger':32,'tablet':0}

{key:value for (key,value) in products.items() if value>0} #outlook: {'phone': 10, 'charger': 32}


# Nested Comprehension
# print tables of number from 2 to 4

{
    2:{1:2,2:4,3:6,4:8},
    3:{1:3,2:6,3:9,4:12},
    4:{1:4,2:8,3:12,4:16}
}

{i:{j:i*j for j in range(1,11)} for i in range(2,5)}