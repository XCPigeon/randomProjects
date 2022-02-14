#######################
### GUESS A NUMBER  ###
#######################
#written by Andrew Snodgrass

# Our goal with this program will be to get the
# user to guess a number that the computer generates
#######
# sudo code:
# make a random number
# while: the user hasn't guessed it
    # make them guess
    # tell them if they are high or low
# Tell them they got it!
from random import randint

def guess_check(x,y):
    if x > y:
        print("Sorry, that guess is too high!")
        return "high"
    if x < y:
        print("Sorry, that guess is too low!")
        return "low"
    else:
        return "right"


num_check = False
print("Let\'s play a guessing game!\n I\'ll choose a number and you try to guess it!!")

while num_check == False: # this while loop is to check if the number given by
    max_num = int(input("What number should I go up to (2 or greater) ?")) # ask for number
    if not (max_num >= 2):
        print("No, seriously, I need a number 2 or over.")
    else:
        num_check = True
number = randint(1,max_num)
guess = -1
guess_stat = ""
while guess_stat != "right":
    guess = int(input("What is your guess? "))
    guess_stat = guess_check(guess, number)
print (f"That's right! The number was {number}!!!!")

