#----------------------------------------------------------------------
#SECTION 14: STRINGS IN PYTHON : STRING FUNCTIONS (PART 5)
#----------------------------------------------------------------------

#COMMON FUNCTIONS IN STRING

# Python provides several built-in functions that can operate on strings. Some commonly used functions are:
#
# len()
# max()
# min()
# sorted()


#----------------------------------------------------------------------
# LENGTH -> len()
#----------------------------------------------------------------------

# len() returns the total number of characters in a string. Spaces are also counted as characters.

city = "Kolkata"

print(len(city)) # Output:  7

#----------------------------------------------------------------------
# MAXIMUM VALUE -> max()
#----------------------------------------------------------------------

# max() returns the character with the highest Unicode value.
# For common English letters, Unicode values are the same as ASCII values.

city = "Kolkata"

print(max(city)) # Output: 't', Unicode Values: K = 75 | o = 111 | l = 108| k = 107| a = 97 | t = 116 | a = 97 


#----------------------------------------------------------------------
# MINIMUM VALUE -> min()
#----------------------------------------------------------------------

# min() returns the character with the lowest Unicode value.

city = "Kolkata"

print(min(city))

# Output: 'K', Reason: Capital letters have smaller Unicode values than lowercase letters. K = 75 | a = 97

#----------------------------------------------------------------------
# SORTED -> sorted()
#----------------------------------------------------------------------

# sorted() sorts the characters of a string in ascending order based on Unicode values.
# IMPORTANT:
# sorted() does NOT return a string.
# It returns a LIST.

city = "Kolkata"

srt = sorted(city)

print(srt) # Output: ['K', 'a', 'a', 'k', 'l', 'o', 't']


#----------------------------------------------------------------------
# SORTED IN DESCENDING ORDER
#----------------------------------------------------------------------

# reverse=True sorts the characters in descending order.

srt_desc = sorted(city, reverse=True)

print(srt_desc)

# Output:
# ['t', 'o', 'l', 'k', 'a', 'a', 'K']


#----------------------------------------------------------------------
# IMPORTANT INTERVIEW POINT
#----------------------------------------------------------------------

# sorted() returns a LIST, not a STRING.

city = "Kolkata"

result = sorted(city)

print(type(result)) # Output: <class 'list'>

# If you want the result as a string:

result = ''.join(sorted(city))

print(result) # Output:  Kaaklot


#----------------------------------------------------------------------
# UNICODE / ASCII BEHAVIOR
#----------------------------------------------------------------------

# Capital letters come before lowercase letters because they have smaller Unicode values.

print(sorted("aAbB")) # Output: ['A', 'B', 'a', 'b']

# Unicode Values:
#
# A = 65
# B = 66
# a = 97
# b = 98

#----------------------------------------------------------------------
# QUICK SUMMARY
#----------------------------------------------------------------------

# len("Kolkata")
# Output -> 7
#
# max("Kolkata")
# Output -> 't'
#
# min("Kolkata")
# Output -> 'K'
#
# sorted("Kolkata")
# Output -> ['K', 'a', 'a', 'k', 'l', 'o', 't']
#
# sorted("Kolkata", reverse=True)
# Output -> ['t', 'o', 'l', 'k', 'a', 'a', 'K']

#FUNCTION APPLICABLE EXCLUSIVELY TO STRINGS -> 
# 
# 1. Capitalize, Title, Upper, Lower, Swapcase

e = 'west bengal'

e.capitalize() #The capitalize function makes the word into proper case for the first word. It will not change the original string

print(e) #output: west bengal

e.title()# This makes each word in the sentence a proper case. -> West Bengal

e.upper()# output : WEST BENGAL. All the letters are in upper case

e.lower()# Output: west bengal. All the letter will be in the lowe case.

z = "aYAN mITRA"

z.swapcase() #output 'Ayan Mitra'. Converts lower case to upper and uppercase to lower.

# 2. COUNT FUNCTION : Provides the count of  a particular substring

no_of_str = "How is the weather in Delhi?"

no_of_str.count('i') #output: 3

#this also works on sub string as well

no_of_str.count('he') #output: 2

# 3. Find/Index

#Find retrieves the first occurences of the letter/string in question

no_of_str.find('w') #output: 2. Retrieves the first occurence of the letter

no_of_str.index('w') #output: 2. Retrieves the first occurence of the letter like find however throws an error if the letter is not present.

#4. endswith/startswith
no_of_str.endswith('Delhi?')# output TRUE

no_of_str.startswith('How')# output TRUE

#5. format : when we are not sure what values will be used we can use format function

"Hello my name is {} and I work as as {} for HCLTECH".format("Ayan","AI Consultant")

#output: 'Hello my name is Ayan and I work as as AI Consultant for HCLTECH'

"Hello my name is {1} and I work as as {0} for HCLTECH".format("Ayan","AI Consultant")

#output: 'Hello my name is AI Consultant and I work as as Ayan for HCLTECH'

"Hello my name is {name} and I work as as {position} for HCLTECH".format(name = "Ayan", position = "AI Consultant")

#6. isalnum/isalpha/isdecimal/isdigit/isidentifier. this are used for asking questions

wrd = "FLAT10"
wrd_1 = "FLAT10$"
wrd_2 = "FLAT"

wrd.isalnum() #output : True, asking if the variable contains alphabets or numbers.

wrd_1.isalnum() #Output: False, contains a special charater $

wrd_2.isalpha() #output : True, asking if the variable contains only alphabets.

wrd.isalpha()#output : False, asking if the variable contains only alphabets.

dig = 20
dig_1 = "20"
dig_2 = "34R"

dig.isdigit() #output:Error. 'int' object has no attribute 'isdigit'

dig_1.isdigit() #Output: True. Here the string is being tasted if it is a digit

dig_2.isdigit() #output: False.the digit contains a letter as well as a result this is False

#7. SPLIT() in String

#The split funtion converts the string to list

nat = "Who is the Prime Minister of India in 2026?"

nat.split() #output: ['Who', 'is', 'the', 'Prime', 'Minister', 'of', 'India', 'in', '2026?']

nat.split('i') #output: ['Who ', 's the Pr', 'me M', 'n', 'ster of Ind', 'a ', 'n 2026?']

#8 join() function is the reverse of split function. So if we have a list we can convert it back to a string. 

ion = ['Who', 'is', 'the', 'Prime', 'Minister', 'of', 'India', 'in', '2026?']

" ".join(ion) #Output with space: 'Who is the Prime Minister of India in 2026?'

"*".join(ion) #Output with asterix:'Who*is*the*Prime*Minister*of*India*in*2026?'

#9. replace() is used to replace an exisiting sub string with some other sub strin

ufo = "I like to play foothball"

ufo.replace('foothball', 'PC GAMES') # Output: 'I like to play PC GAMES'

#10. strip() is used to remove the trailing and leading spaces

name = "    AYAN"
title = "MITRA"
gender = "  Male    "

print("Hi",name,"Is your title", title) #Output: Hi     AYAN Is your title MITRA

NAME =name.strip()
print(NAME)

TITLE = title.strip()
print(TITLE)

GENDER = gender.strip()

print(GENDER)






