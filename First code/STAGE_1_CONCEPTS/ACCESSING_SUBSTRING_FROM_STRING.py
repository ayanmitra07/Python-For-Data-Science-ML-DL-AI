#---------------------------------------------------------------
# SECTION 14: STRING IN PYTHON: ACCESSING SUBSTRINGS (PART 2)
#---------------------------------------------------------------

# ACCESSING SUBSTRINGS FROM A STRING using Indexing and Slicing:

#Concept of Indexing:
# In Python, strings are indexed, which means that each character in a string has a unique
# position (index) that can be used to access it. The index of the first character is 0, the 
# second character is 1, and so on.
#Indexing is of two types: positive indexing and negative indexing. Positive indexing starts 
# from the leftmost character, while negative indexing starts from the rightmost character.
# Negative indexing is also supported, where the last character has an index of -1, the second to last 
# character has an index of -2, and so on.

#Positive Indexing:

f = "MANGO"

print(f[2]) # Output: N (the character at index 2 is 'N')

#Negative Indexing:

print(f[-2]) # Output: G (the character at index -2 is 'G')

#Concept of Slicing:
# In Python, you can access substrings from a string using slicing. here we can extract multiple 
# characters from a string by specifying a range of indices.
# The syntax for slicing is: string[start:end:step]
# - start: The index where the slice starts (inclusive). If omitted, it defaults to 0.
# - end: The index where the slice ends (exclusive). If omitted, it defaults to the length of the string.
# - step: The step size for slicing. If omitted, it defaults to 1.

sli = "SUPER MARIO"

print(sli[0:5])  # Output: SUPER (characters from index 0 to 4)

print(sli[2:])  # Output: PER MARIO (characters from index 2 to the end of the string)

print(sli[:4]) # Output: SUPE (characters from the beginning of the string to index 3)

print(sli[:]) # Output: SUPER MARIO (the entire string)

print(sli[2:7:2]) # Output: PRM (characters from index 2 to 6 with a step of 2, which gives us 'P' and 'R' from "PER M" and 'M' from "MARIO")

print(sli[0:7:-1]) #Output: empty string (since the step is negative, the start index should be greater than the end index for it to work, but here 0 is less than 7)

print(sli[-5:-1: 2]) #Output: Python will consider MARIO and will slice it from index -5 to -1 (since the end index is exclusive) with a step of 2, which gives us 'M' and 'R'.

print(sli[::-1]) #Output: OIRAM REPUS (the entire string in reverse order)