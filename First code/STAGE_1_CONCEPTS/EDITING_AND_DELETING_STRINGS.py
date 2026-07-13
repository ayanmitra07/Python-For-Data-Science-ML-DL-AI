#----------------------------------------------------------------------
#SECTION 14: STRINGS IN PYTHON : EDITING AND DELETING STRINGS (PART 3)
#----------------------------------------------------------------------


# STRING IMMUTABILITY
# -------------------
# Strings in Python are IMMUTABLE.
#
# Mutable   = Can be changed after creation.
# Immutable = Cannot be changed after creation.
#
# Once a string is created, we cannot modify, add, or delete
# individual characters from the existing string.

# Example: Editing a character in a string

city = "Kolkata"

# city[0] = "C"
# ERROR:
# TypeError: 'str' object does not support item assignment
#
# Reason:
# Python does not allow modification of individual characters
# because strings are immutable.

print(city)  # Kolkata


# REASSIGNMENT IS ALLOWED
# -----------------------
# Although strings are immutable, variables can be reassigned.
#
# In reassignment, we are NOT changing the existing string.
# We are simply making the variable point to a NEW string object.

city = "Calcutta"

print(city)  # Calcutta


# ADDING CHARACTERS TO A STRING
# -----------------------------
# We cannot add a character directly to a specific position
# in an existing string.

word = "YELLO"

# word[5] = "W"
# ERROR:
# TypeError: 'str' object does not support item assignment
#
# Reason:
# Python treats this as modifying the existing string.

# Correct Way:
# Create a NEW string using concatenation.

word = word + "W"

print(word)  # YELLOW


# DELETING AN ENTIRE VARIABLE
# ---------------------------
# The 'del' keyword can delete a variable reference.

city = "Calcutta"

del city

# print(city)
# ERROR:
# NameError: name 'city' is not defined
#
# Reason:
# The variable no longer exists.


# DELETING A SINGLE CHARACTER
# ---------------------------
# Python does not allow deletion of individual characters
# from a string because strings are immutable.

text = "TRANSFORMERS"

# del text[0]
# ERROR:
# TypeError: 'str' object doesn't support item deletion

print(text)


# DELETING A SLICE OF A STRING
# ----------------------------
# Python does not allow deletion of a portion of a string.

# del text[:3:2]
# ERROR:
# TypeError: 'str' object doesn't support item deletion

print(text)


# IMPORTANT INTERVIEW POINT
# -------------------------
# Strings are immutable, but variables are not.
#
# Example:

x = "DATA"

x = x + " SCIENCE"

print(x)  # DATA SCIENCE

# Why does this work?
#
# Step 1:
# x points to the string "DATA"
#
# Step 2:
# Python creates a NEW string "DATA SCIENCE"
#
# Step 3:
# Variable x is reassigned to the new string.
#
# The original string is never modified.
#
# Therefore:
# - String remains immutable.
# - Variable reassignment is allowed.


# REAL-WORLD ANALOGY
# ------------------
# Think of a string as a printed PDF document.
#
# Once printed:
# You cannot change a single letter.
# You cannot delete a few letters.
# You cannot insert letters in the middle.
#
# You can create a completely new PDF with the desired changes.
#
# Python strings behave in the same way.