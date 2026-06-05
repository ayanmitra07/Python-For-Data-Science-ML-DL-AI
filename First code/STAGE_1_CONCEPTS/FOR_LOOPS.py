#---------------------------------------------
#SECTION 9: FOR LOOPS
#---------------------------------------------

#FOR LOOPS: A for loop is a control flow statement that allows you to repeat a block of code 
# a certain number of times. It is often used to iterate over a sequence (like a list, tuple, or string) 
# or to execute a block of code a specific number of times.

#Before we dive into for loops, let's quickly review the concept of a range in Python.
# The range function is a built-in function used to generate a sequence of numbers. 
# It can take one, two, or three arguments: start, stop, and step.

#range function

from shutil import which


range(1,11) # This will generate numbers from 1 to 10 (stop is exclusive) intrnally it creates 
            #a list of numbers from 1 to 10 but it does not store it in memory, 
            # it generates the numbers on the fly when needed.

print(list(range(1,11))) # This will convert the range object into a list, 
                            # which will store all the numbers in memory.

#end of range function

print(list(range(5))) # This will generate numbers from 0 to 4 (stop is exclusive)

#Step argument in range function

print(list(range(1,11,2))) # This will generate numbers from 1 to 10 with a step of 2,
                    # which means it will generate odd numbers from 1 to 10.

#Sequence: A sequence is an ordered collection of items. In Python, there are several types of sequences,
# including lists, tuples, and strings.

var = "kolkata" # This is a string sequence, which is an ordered collection of characters.

var1 = ["apple", "banana", "cherry"] # This is a list sequence, which is an ordered collection of items.

var2 = ("red", "green", "blue") # This is a tuple sequence, which is an ordered collection of items.

#Python itertes over the range or sequence and executes the block of code for each item in the range or sequence.

#iteration of for loop over a range

for i in range(1, 11):
    print(i) # This will print numbers from 1 to 10 (stop is exclusive)

#Backward iteration

for i in range(10,0,-2):
    print(i) # This will print numbers from 10 to 1 with a step of -2, which means it will print even numbers from 10 to 1.

#Iteration on string sequence

for i in "kolkata":
    print(i) # This will print each character in the string "kolkata" on a new line.

#When to use WHile loop and when to use FOR loop
#Use a for loop when you know the number of iterations in advance or when you want 
# to iterate over a sequence (like a list, tuple, or string).

#Use a while loop when you want to repeat a block of code until a certain condition is met, 
# here we do not know how many times the loop will go on, it depends on the condition.