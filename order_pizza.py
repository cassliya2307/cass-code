table = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|Pizza Type	|Number of slice|Price per box	|		
|_______________|_______________|_______________|			
|Sapa size	|4		|N2,500		|
|_______________|_______________|_______________|
|Small money	|6		|N2,900		|
|_______________|_______________|_______________|
|Big boys	|8		|N4,000		|
|_______________|_______________|_______________|
|Odogwu		|12		|N5,200		|
|		|		|		|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

		"""
print(table)
pizzaType = input("Enter the type of pizza: ")

match pizzaType:
	case "sapa size":
		people = int(input("Enter the number of people: "))
		slices = 4
		pizza = 0 
		price = 0
		boxes = people // slices
		remain = people % slices
		remainder = 0
		
		if remain < 4 and remain != 0:
			boxes = boxes + 1
			pizza = slices * boxes
			price = 2500 * boxes
			remainder = pizza - people

		else:
			boxes = people / slices
			price = slices * boxes
			remainder = pizza - people


		print("Number of boxes of pizza to buy = " , boxes)
		print("Sapa size contains 4 slices per box " , boxes , " should be enough for " , people , " people as it would contain " , pizza , " slices in all.")

		print("Number of slices left = " , remainder)
		print("Price = N" ,price )


	case "small money":
		people = int(input("Enter the number of people: "))
		slices = 6
		pizza = 0 
		price = 0
		boxes = people // slices
		remain = people % slices
		remainder = 0
		
		if remain < 6 and remain != 0:
			boxes = boxes + 1
			pizza = slices * boxes
			price = 2900 * boxes
			remainder = pizza - people

		else:
			boxes = people / slices
			price = slices * boxes
			remainder = pizza - people


		print("Number of boxes of pizza to buy = " , boxes)
		print("Small money contains 6 slices per box " , boxes , " should be enough for " , people , " people as it would contain " , pizza , " slices in all.")

		print("Number of slices left = " , remainder)
		print("Price = N" ,price )



	case "big boys":
		people = int(input("Enter the number of people: "))
		slices = 8
		pizza = 0 
		price = 0
		boxes = people // slices
		remain = people % slices
		remainder = 0
		
		if remain < 8 and remain != 0:
			boxes = boxes + 1
			pizza = slices * boxes
			price = 4000 * boxes
			remainder = pizza - people

		else:
			boxes = people / slices
			price = slices * boxes
			remainder = pizza - people


		print("Number of boxes of pizza to buy = " , boxes)
		print("Big boys contains 8 slices per box " , boxes , " should be enough for " , people , " people as it would contain " , pizza , " slices in all.")

		print("Number of slices left = " , remainder)
		print("Price = N" ,price )




	case "odogwu":
		people = int(input("Enter the number of people: "))
		slices = 12
		pizza = 0 
		price = 0
		boxes = people // slices
		remain = people % slices
		remainder = 0
		
		if remain < 12 and remain != 0:
			boxes = boxes + 1
			pizza = slices * boxes
			price = 5200 * boxes
			remainder = pizza - people

		else:
			boxes = people / slices
			price = slices * boxes
			remainder = pizza - people


		print("Number of boxes of pizza to buy = " , boxes)
		print("Odogwu contains 12 slices per box " , boxes , " should be enough for " , people , " people as it would contain " , pizza , " slices in all.")

		print("Number of slices left = " , remainder)
		print("Price = N" ,price )






	case _: print("Invalid Input");










