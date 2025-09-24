#prompt the user to enter three grades
#save them in separate variables
#determine the average and save it in a variable
#check if the average is less than or equals to 90 and less than or equals to 100, if it is display "A"
#check if the average is less than or equals to 80 and less than 90, if it is display "B"
#check if the average is less than or equals to 70 and less than 80, if it is display "C"
#check if the average is less than or equals to 60 and less than 70, if it is display "D"
#check if the average is less than or equals to 0 and less than 60, if it is diaplay "E"

first = int(input("Enter first grade: "))

second = int(input("Enter second grade: "))

third = int(input("Enter third grade: "))

 average = first + second + third / 3


if average <= 90 and average <= 100:

	print("A")


elif average <= 80 and average < 90:

	print("B")



elif average <= 70 and average < 80:

	print("C")



elif average <= 60 and average < 70:

	print("D")



elif average <= 0 and average < 60:

	print("E")



