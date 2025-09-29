binary = int(input("Enter a binary number: "))

decimal_value = 0
power = 0

while binary > 0:
    last_digit = binary% 10  
    decimal_value += last_digit * (2 ** power)
    binary //= 10  
    power += 1

print("Decimal equivalent:", decimal_value)