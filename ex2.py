# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.  
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#
#    If the number is a multiple of 4, print out a different message.
#    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#! bin/bash python

numb = int(input("Gimmie a Positive Whole Number"))
if (numb%2==0):
  msg= "EVEN"
elif (numb%4==0):
  msg= "Even and divisiable by 4"
else:
  msg = "ODD"

num = double(input("okay last bit. Give me a dividend : "))
check = double(input("ok.... now the divisor : "_))
if (check%num==0):
  divi = "evenly"
else:
  divi = "not evenly"
print (("the whole number you gave me is {} and your numbers devide {}").format(msg,divi))
