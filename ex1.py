###########################################################################################################################################
# Found :
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that
#  they will turn 100 years old.
#
# Extras:
#    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
#         (Hint: order of operations exists in Python)
#    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
###########################################################################################################################################
#! /bin/bash Python

#originalAssignment():
name = input("Hello How Young Are You? : \n")
age = input("What Is Your Age? : \n")
age = int(age)

#calc 100
year = 2018+(100-age)

msg= (("Hello {} You will be 100 years old int the year {}").format(name.title(),year))

print (msg)
##########################################################################################################################################
## extra add on 1 
##########################################################################################################################################
repeat=int(input("How many copies of the message would you like?: "))
  print (msg*repeat)
  
##########################################################################################################################################
## extra add on 2
##########################################################################################################################################
print (repeat*(msg+ "/n")
