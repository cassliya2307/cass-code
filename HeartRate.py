age = int(input("Enter your age: "))

heart_rate = 220 - age
low_heart_rate = 0.5 * heart_rate
high_heart_rate = 0.85 * heart_rate

print("Your maximum heart rate is", high_heart_rate)
print("Your minimum heart rate is", low_heart_rate)  