"""
Written by Andrew Snodgrass
This program *should* take a file named "garbageData.txt" of numbers separated by spaces or new lines, find the sum,
mean, and stdev. Then it will sort them into groups A,B,C,D based on 0-25, 26-50, etc to 100 and output that data to
console and a file named "myOutput.txt".

I struggled a ton with variable types with this project more than anything. I found that once you have a list that
you like, make a new list with list(map(<var_type> . This will make future calculations much easier.
"""

### Stuff we need ###
from statistics import stdev  # for std deviation

holder = ""  # temp holding for reading the file
first_array = []  # to input the garbage from file
final_list = [0, 0, 0]  # to dump our answers into
dic = len(open("garbageData.txt").read())  # stores the whole length of the file

### READ FILE ###
with open("garbageData.txt") as inputt:
    count = 0
    while count <= dic:  # while there are still characters in the file
        count += 1
        cur = inputt.readline(1)  # read the current character we are on
        if cur != " " and cur != "\n": # if the character is not a space or new line, add to the holding variable
            holder += cur
        else:  # if it is a space/newline, add the number we got to the array, reset holder
            first_array.append(holder)
            holder = ""
first_array_but_int = list(map(int, first_array))  # used this to convert the list into all ints
print("Finished reading the file!")

### CALC SUM ###
i = 0
length = len(first_array_but_int)  # I'm sure there's a more elegant way to do this, but i'm too lazy to find it.
while i < length:
    final_list[0] += first_array_but_int[i]  # this loop is just adding the numbers one after another
    i += 1

### CALC MEAN ###
final_list[1] = final_list[0] / len(first_array_but_int)  # this takes the sum of all and divides by amount (mean)

### STANDARD DEV ###
final_list[2] = stdev(first_array_but_int)  # Got lazy with this too

### FINISH ###
print("The sum of the file is ", str(final_list[0]), "\nThe average was ", str(final_list[1]), "\nAnd the stdev was ",
      str(final_list[2]))  # prints out the list nicely

### RANGES AND OUTPUT ###
# This is abcd, up to 100
file = open("myOutput.txt", "w+")
ranges = [int(0), int(0), int(0), int(0)]
i = 0
for i in range(len(first_array_but_int)):
    if first_array_but_int[i] > 75:  # if the number is in this section:
        ranges[3] += 1  # Adds one to the total count for the end
        print(str(first_array_but_int[i]) + ": D")  # Prints to console what each number is
        file.write(str(first_array_but_int[i]) + ": D\n")  # Prints to file what each number is
    elif first_array_but_int[i] > 50:
        ranges[2] += 1
        print(str(first_array_but_int[i]) + ": C")
        file.write(str(first_array_but_int[i]) + ": C\n")
    elif first_array_but_int[i] > 25:
        ranges[1] += 1
        print(str(first_array_but_int[i]) + ": B")
        file.write(str(first_array_but_int[i]) + ": B\n")
    else:  # basically if under 25
        ranges[0] += 1
        print(str(first_array_but_int[i]) + ": A")
        file.write(str(first_array_but_int[i]) + ": A\n")

### OUTPUT RANGES ###
file.write("\n\n\nTOTALS:")
file.write("\nA: " + str(ranges[0]))
file.write("\nB: " + str(ranges[1]))
file.write("\nC: " + str(ranges[2]))
file.write("\nD: " + str(ranges[3]))
file.close()
