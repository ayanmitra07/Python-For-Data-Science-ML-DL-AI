#-------------------------------------------------
#SECTION 6: IF ELSE STATEMENT
#-------------------------------------------------

#The if statement is used to test a condition. If the condition is true, 
# the block of code inside the if statement is executed. If the condition is false, 
# the block of code inside the if statement is skipped.
# The else statement is used to execute a block of code if the condition in the if statement is false.
# The elif statement is used to test multiple conditions. It stands for "else if".

# So If-else is used to control the flow of the program based on certain conditions. 
# It allows you to execute different blocks of code based on whether a condition is true or false.
#it is used when our program arrives at branching point and we want to execute different code based
# on the condition. For example, if we want to check if a number is positive, negative or zero, 
# we can use if else statement.

#Dummy login system
#correct email is ayan.mitra.epba@iim.cal.in
#correct password is 12345

email = input("Provide your iim email id: ")
password = input("Insert your password: ")

if email =="ayan.mitra.epba@iim.cal.in" and password == "12345":
    print("Welcome Ayan!")
elif email == "ayan.mitra.epba@iim.cal.in" and password != "12345":
    print("Password is incorrect")
    password = input("Insert your password again: ")
    if password == "12345":
        print("Correct Password!")
    else:
        print("Still incorrect")
else:
    print("Invalid email or password. Please try again.")
