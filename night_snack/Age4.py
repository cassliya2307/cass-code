#Prompt the user to enter two things:
	#The father's age 
	#The son's age 
#save both of them in a variable
#initialize another variable to store the number of years and assign value o to it
#initialize another variable to store the son's age times 2
#Check if the fathers age is greater than twice the son's age, if it is
#Determine how many years ago the fathers age was twice the sons age and display the number of years, if not
#Check if the fathers age is less than twice the sons age, if it is
#Determine the number of years it will take for the fathers age to be twice the sons age and display the number of years, if not
#initialize a variable year two that is equal to zero and display it if the father's age is equal to twice the son's age*/

father = int(input("Enter father's age: "))
son = int(input("Enter son's age: "))

years = 0
son2 = son * 2

if father > son2:

	years = father - 2 * son
	print("The number of years is" + years + " yrs")





elif father < son2:

	years = 2 * son - father
	print("The number of years is" + years + "yrs")





elif father == son2:

	int years1 = 0
	print("The number of years is" + years1 + " yrs")






