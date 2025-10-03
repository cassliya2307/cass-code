def my_discount(price, discount):
	discount = price * discount / 100
	return price - discount



price = int(input("Enter the price"))
discount = int(input("Enter the discount"))
print(my_discount(price,discount))