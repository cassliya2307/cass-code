max_side = 20

print("Pythagorean triples (side1, side2, hypotenuse) up to 20:")

for side1 in range(1, max_side + 1):
    for side2 in range(side1, max_side + 1):  
        for hypotenuse in range(side2, max_side + 1): 

            if side1**2 + side2**2 == hypotenuse**2:
                print(side1,side2,hypotenuse)