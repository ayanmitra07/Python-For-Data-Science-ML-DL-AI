#-------------------------------------------------------
#SECTION 10: NESTED LOOPS
#-------------------------------------------------------

#Nested loops: A nested loop is a loop that is inside another loop.
# The inner loop will be executed for each iteration of the outer loop.
#We use nested loops when we want to perform a task that requires multiple levels of iteration.
# the nested loops is not a ggod practise due to time complexity,
#  it can lead to a large number of iterations and can make the code difficult to read and understand.
#the more the number of nested loops, the more complex the code becomes and the harder it is to debug 
# and maintain.

#a program where we built a social media where we need to find out the total number of friends for each user 
# So we will require a loop to find out each user and another loop to find out the number of friends
#  for each user.


#printing a pattern using nested loops

rows = int(input("Enter the number of rows: "))

for i in range(1, rows +1): # This will iterate from 1 to the number of rows (inclusive)
    for j in range(0, i): # This will iterate from 0 to i-1 (inclusive)
        print("*", end = " ") # This will print * without a new line and with a space in between
    print() # This will print a new line after each row is printed