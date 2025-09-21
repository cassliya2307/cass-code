//prompt the user to enter three integers
//save them in separate variables
//determine and display their sum
//determine and display their average
//Check if the first number is greater than the other two, if it is
//display it as the largest, if not
//Check if the second number is greater than the other two, if it is
//display it as the largest, if not
//Check if the third number is greater than the other two, if it is
//display it as the largest
//Check if the first number is less than the other two, if it is
//display it as the smallest, if not
//Check if the second number is less than the other two, if it is
//display it as the smallest, if not
//Check if the third number is less than the other two, if it is
//display it as the smallest, if not







num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer:"))
num3 = int(input("Enter third integer: "))

sum = num1 + num2 + num3

average = sum / 3

print(sum)
print(average)

if num1<num2 and num1<num3:

	print(num1," is the smallest")

elif num2<num3 and num2<num1:

	print(num2," is the smallest")

elif num3<num2 and num3<num1:

	print(num3," is the smallest")



if num1>num2 and num1>num3:

	print(num1," is the largest")

elif num2>num1 and num2>num3:

	print(num2," is the largest")

elif num3>num2 and num3>num1:

	print(num3," is the largest")

