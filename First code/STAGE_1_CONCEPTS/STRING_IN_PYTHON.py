#---------------------------------------------------------------
# SECTION 14: STRING IN PYTHON (PART 1)
#---------------------------------------------------------------

# STRING IN PYTHON:
# A string is a sequence of Unicode characters enclosed in either
# single quotes (' ') or double quotes (" ").
#
# Strings are used to represent text in Python and can contain letters,
# numbers, symbols, and whitespace characters.
#
# Strings are immutable, which means that once a string is created,
# its contents cannot be changed. However, new strings can be created
# through operations such as concatenation, slicing, or replacement.
#
# Why Unicode characters?
# Computers ultimately store and process data as binary numbers (0s and 1s).
# To represent text, each character is assigned a unique numeric code.
#
# Python uses the Unicode standard, which provides numeric codes for
# characters from many languages and writing systems around the world.
#
# When a string is stored in memory, its Unicode code points are encoded
# into bytes (such as UTF-8 or UTF-16), which are then represented as binary
# data that the computer can process.
#
# Using Unicode allows Python programs to work with text from different
# languages, making internationalization and localization possible.

# We can use both double quotes and single quotes to create strings in Python. this is so that we avoid any errors
# when we want to include a single quote or double quote within the string itself.

city = "Kolkata"  # Using double quotes to create a string
name = 'Ayan'  # Using single quotes to create a string

sen = "It's a beautiful day!"  # Using double quotes to include a single quote in the string
quote = 'She said, "Hello!"'  # Using single quotes to include double quotes in the string

# This will cause a syntax error because the single quote in "It's" is interpreted as the end of the string

#wrng = 'She said, It's a beautiful day!' 

print(city)  # Output: Kolkata
print(name)  # Output: Ayan 
print(sen)   # Output: It's a beautiful day!
print(quote) # Output: She said, "Hello!"

#MULTILINE STRINGS: In Python, you can create multiline strings using triple quotes (''' ''' or """ """).
# This allows you to include line breaks and preserve the formatting of the string.

f = '''This is a multiline string in single quotes.'''
g = """This is a multiline string in double quotes."""

print(f)  # Output: This is a multiline string in single quotes.
print(g)  # Output: This is a multiline string in double quotes.

#Creating string with type conversion functions: You can also create strings by converting other 
# data types to strings using the str() function.

num_to_str = str(234)

print(type(num_to_str))  # Output: <class 'str'>, the string representation of the number 234