#----------------------------------------------
#Section 8: Guessing Game
#----------------------------------------------

# In this section, we will create a simple guessing game where the user has to guess a randomly
#  generated number between 1 and 100.

import random

# Generate a random number between 1 and 100

jackpot = random.randint(1,100)

# User input
guess = int(input("Guess the number"))

#Number of attempts
attempts = 1

# Loop until the user guesses the correct number
while guess !=jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print(("Guess lower"))

    guess = int(input("Guess the number"))
    attempts += 1

print("correct guess!")
print("You took",attempts,"attempts to guess the number")
