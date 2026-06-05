#---------------------------------------------------------------
#SECTION 13: BUILT-IN MODULES
#---------------------------------------------------------------

#BUILT-IN MODULES: You can consider a module as a code library. Python provides a wide range 
# of built-in modules that are pre-installed with the Python standard library. 
# These modules contain functions, classes, and variables that can be used to perform various 
# tasks without the need for external libraries. Some commonly used built-in modules include:

help("modules")  # This will display a list of available modules in Python.

#1. math: This module provides mathematical functions and constants, such as trigonometric functions,
# logarithmic functions, and constants like pi and e. It is commonly used for performing 
# mathematical operations in Python.

import math

math.ceil(4.2)  # Output: 5, rounds a number up to the nearest integer

math.floor(4.2)  # Output: 4, rounds a number down to the nearest integer

math.pi  # Output: 3.141592653589793, the value of pi

math.e # Output: 2.718281828459045, the value of e

math.sqrt(16)  # Output: 4.0, the square root of 16

math.factorial(4)  # Output: 24, the factorial of 4 (4 * 3 * 2 * 1)

#2. random: This module provides functions for generating random numbers, shuffling sequences, and
#   selecting random elements from a list. It is commonly used for tasks such as random sampling 
#   and generating random data.

import random

random.randint(24, 37) # Output: A random integer between 24 and 37 (inclusive)

random.choice(['AYAN', 'ROHIT', 'KANCHAN', 'ABHISHEK']) # Output: A random name from the list

g = [1, 2, 3, 4, 5]
random.shuffle(g) # Output: The list [1, 2, 3, 4, 5] shuffled in random order
print(g) # Output: The shuffled list, e.g., [3, 1, 5, 2, 4]

#3. time: This module provides functions for working with time-related tasks, such as getting the current time,
#   measuring the execution time of code, and creating delays. It is commonly used for tasks 
# such as timing code execution and creating time-based events.

import time

time.time()  # Output: The current time in seconds since the epoch (January 1, 1970)

time.ctime() # Output: The current time in a human-readable format, e.g., 'Mon Sep 27 14:30:00 2021'

print("Hello")

time.sleep(4)  # This will pause the execution of the program for 4 seconds

print("World")  # Output: This will be printed after a delay of 4 seconds

#4. os: This module provides functions for interacting with the operating system, such as file and 
# directory operations, and environment variables. It is commonly used for tasks such as file handling and
# managing the file system. 
# Note: The os module is not available in online coding platforms, so you may not be able to run the code
# examples for this module in such environments. 
# However, you can run the code examples for the os module in a local Python environment on your computer.
# Here are some examples of using the os module:

import os

os.getcwd()  # Output: The current working directory. It stands for "get current working directory"

os.listdir() # Output: Returns a list of files and directories in the current working directory
            # It lists the contents of the current directory and rest of the directory path can be specified 
            # as an argument to list the contents of that directory.   
            # For example, os.listdir('C:/Users/YourUsername/Documents') will list the
            # contents of the Documents directory.
            #if no directory is specified, it lists the contents of the current working directory.