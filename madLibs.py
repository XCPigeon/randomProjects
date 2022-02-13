################
## MAD LIBS   ##
################

# this project is just a madlibs. I'm going to
# try and do like 3 different stories so its different every time.

from random import randint

story = randint(0,2)
def story_Time(x):
    if x == 0:
        storyOne()

    if x == 1:
        storyTwo()

    if x == 2:
        storyThree()

def storyOne():
    noun1 = input("Noun: ")
    place = input("Place: ")
    noun2 = input("Noun: ")
    verb = input("Verb: ")
    print(f"There once was a {noun1}, the best {noun1} there was in all the {place}."
          f"One day he desided to climb the tallest {noun2}, where he would {verb} all day")
    ## There once was a (noun1), the best (noun1) there was in all the (place).
    ## One day he desided to climb the tallest (noun2), where he would (verb).

def storyTwo():
    verb1 = input("Verb: ")
    noun1 = input("Plural of a noun: ")
    noun2 = input("Noun: ")
    verb2 = input("Verb: ")
    noun3 = input("Noun: ")
    print(f"After a long day of {verb1}ing {noun1}, I like to sit down on a {noun2} and {verb2} a {noun3}.")

def storyThree():
    num = input("Number: ")
    noun1 = input("Noun: ")
    verb = input("Verb: ")
    noun2 = input("Noun: ")
    print(f"Sir, the reason I pulled you over was because you were going {num} over in a {noun1} zone."
          f" I\'m going to have to {verb} you a {noun2} for that.")

print("Lets play some madLibs!")
story_Time(story)
print("\nThat was fun!!!")