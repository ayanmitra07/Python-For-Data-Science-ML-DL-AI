#--------------------------------------
#SECTION 1: Keywords and Identifiers
#--------------------------------------

#KEYWORDS
# Python is a case sensitive language, which means 
# that keywords must be written in lowercase. 
# For example, the keyword "if" is different from "If" or "IF". 
# Using the correct case is important to avoid 
# syntax errors in your code.

#In programming, a keyword is a word that is reserved by 
# a program because the word has a special meaning. 
# keywords can be command or parameters. Every programming language has a set of 
# keywords thsat cannot be used as variable name.

#python has 35 keywords, which are:

import keyword
print(keyword.kwlist)

#Identifiers
# A python identifier is a name used to identify 
# a variable, function, class, module or other object.
# Rules for setting an identifier:
#1. An identifier can only contain letters (a-z, A-Z), digits (0-9) and underscores (_).
#2. An identifier must start with a letter or an underscore, but cannot start with a digit.
#3. An identifier cannot be a keyword.
#4. An identifier is case sensitive, which means that "myVariable" and "myvariable" are 
# considered different identifiers.

#1name = "ayan" #invalid identifier, starts with a digit

name1 = "ayan" #valid identifier
_name = "ayan" #valid identifier

print(name1)
print(_name)
#print(1name) #this will raise a syntax error because 1name is an invalid identifier.

