import math
a = -0.5
b = 5
c = -10
T = 0  
c = c - T
D = b**2 - 4*a*c  
if D >= 0:
    t1 = (-b + math.sqrt(D)) / (2*a)
    t2 = (-b - math.sqrt(D)) / (2*a)
    print("Time when temperature is", T, "°C is at:", t1, "or", t2)
else:
    print("No real solution")
