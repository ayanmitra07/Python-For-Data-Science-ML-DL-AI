#---------------------------------------------------------------
#SECTION 11: BREAK, CONTINUE, PASS STATEMENT
#---------------------------------------------------------------

#BREAK STATEMENT: The break statement is used to exit a loop prematurely when a certain condition is met.
# It can be used in both for and while loops. When the break statement is executed, the loop is terminated,
# and the program continues with the next statement after the loop.

for i in range(1, 11):
    if i == 5:
        break
    print(i)

# in scenarios where the break statement can be use may be linear search, 
# where we want to find a specific item in a list and we can break the loop once we find the item.
# this will improve the runtime of the program as we will not be iterating through the entire list
#  once we find the item.

#######################################################################

#CONTINUE STATEMENT: The continue statement is used to skip the current iteration of a 
# loop and move on to the next iteration. It can be used in both for and while loops.
#  When the continue statement is executed, the rest of the code inside the loop for the 
# current iteration is skipped, and the loop continues with the next iteration. 

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#In scenarios where the continue statement can be used may be when we want to skip certain items in a list
#  while iterating through it. For example, if we are makin an e commerce website and we want to display
#  all the products except the ones that are out of stock, we can use the continue statement to skip the
#  out of stock products while iterating through the list of products.

#######################################################################

#PASS STATEMENT: The pass statement is a null statement that does nothing. 
# It is used as a placeholder. It can be used in situations where a statement is required 
# syntactically but you do not want to execute any code.
# Suppose we are using a for loop to iterate through a list of items, but we have not yet decided what 
# to do with the items in the loop. In this case, we can use the pass statement as a placeholder 
# until we decide what to do with the items in the loop.

for i in range(1, 11):
    if i == 5:
        pass
    print(i)