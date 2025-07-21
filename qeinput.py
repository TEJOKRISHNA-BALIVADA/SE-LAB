import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
T = float(input("Enter temperature to find: "))
c = c - T
D = b**2 - 4*a*c
if D >= 0:
    t1 = (-b + math.sqrt(D)) / (2*a)
    t2 = (-b - math.sqrt(D)) / (2*a)
    print("Time when temperature is", T, "°C is at:", t1, "or", t2)
else:
    print("No real solution")
