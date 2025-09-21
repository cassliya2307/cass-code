#prompt the user to enter a number 
#save it in a variable
#check if it is an even number, if it is
#display "EVEN"
#check if it is an odd number, if it is
#display "ODD"

num = int(input("Enter a number: "))


if num % 2 == 0:

	print("EVEN")

if num % 2 != 0:

	print("ODD")