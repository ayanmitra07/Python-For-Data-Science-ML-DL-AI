# -----------------------------------------------

# SECTION 7: WHILE LOOPS

# -----------------------------------------------

# A while loop is a control flow statement that allows a block of code to execute repeatedly
# as long as a given condition evaluates to True.
# The loop continues running while the condition remains True.
# Once the condition becomes False, the loop stops and the program moves to the next statement after the loop.

# Real-World Analogy:

# Suppose we have an e-commerce webpage where we are searching for MI mobile phones.
# The search returns around 1,000 products.
# The area on the webpage where the details of each mobile phone are displayed is called a container.
# If we compare the containers of two different mobile phones, we may notice that:

# - The images are different.
# - The product descriptions are different.
# - However, the layout and structure of the container are the same.
# Now imagine that we are the developers creating this webpage.

# Should we create 1,000 separate containers for 1,000 products?

# No, that would be highly inefficient.
# For example:

# - If 50 new phones are launched, we would need to create 50 additional containers.
# - If 50 phones are removed, we would need to remove 50 containers.
# This approach would be difficult to maintain.
# Instead, developers create only one container template.
# Then, using a loop (such as a while loop), data is fetched from the database one product at a time.

# The loop repeatedly:

# 1. Retrieves a product from the database.

# 2. Places the product's information into the container.

# 3. Displays the product on the webpage.

# 4. Moves to the next product.

# The process continues until all products have been displayed.

# In simple terms:

# A while loop allows us to perform the same task repeatedly without writing the same code again and again.
# It keeps running until there are no more products left to process, making the program efficient and scalable.

#Prepare a program where user will be asked which tables they want to see, and the program will print 
# the tables until the user says stop.

number = int(input("Which tables do you want to learn?"))

i=1
while i<11: #while condition
    print(number,"*", i,"=", number*i) #body of the loop

    i+= 1 #incrementing the value of i by 1, otherwise it will be an infinite loop.
