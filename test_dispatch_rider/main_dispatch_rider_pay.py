from dispatch_riders_pay_function import*

main ="""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Collection    Amount Per	   Base Pay
   ____rate_____|____Parcel____|_____________
 1.less than 50%|     160      |    5000     =
 ==             |	       |             =
 2. 50 - 59%    |     200      |    5000     =
 ==             |              |             =
 3. 60 - 69%    |     250      |    5000     =
 ==	        |	       |             = 
 4. 70 - 100%   |     500      |    5000     =
 ==             |              |             =
 0. End
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
value = True
while value:	
	print(main)
	package_delivered = int(input("Enter number from the menu: "))

	match package_delivered:
		case 1:
			rate = int(input("Enter number of successful deliveries: "))
			
			while rate > 50:
				print("Number must be in range 1-50")
				rate = int(input("Enter number of successful deliveries: "))
				
			print("N",get_dispatch_riders_pay(rate))

		case 2:
			rate = int(input("Enter number of successful deliveries: "))

			while rate < 50 or rate >= 60:
				print("Number must be in range 50-59")
				rate = int(input("Enter number of successful deliveries: "))
			print("N",get_dispatch_riders_pay(rate))

		case 3:
			rate = int(input("Enter number of successful deliveries: "))

			while rate < 60 or rate >= 69:
				print("Number must be in range 60-69")
				rate = int(input("Enter number of successful deliveries: "))
			print("N",get_dispatch_riders_pay(rate))


		case 4:
			rate = int(input("Enter number of successful deliveries: "))

			while rate < 70:
				print("Number must be in range 70-100")
				rate = int(input("Enter number of successful deliveries: "))
			print("N",get_dispatch_riders_pay(rate))

		
		case 0: value = False