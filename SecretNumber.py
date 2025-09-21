#Create a variable and store a secret number seven in it
#prompt the user to guess a number and save it in a variable
#check if the number they picked is the same with your secret number
#if it is display "That's my favorite number!"
#if not display "Nice try, guess again!"


secret_number = 7

num = int(input("Enter a number: "))

if num == 7:

	print("That's my favorite number!")

else:

	print("Nice try, guess again!")
