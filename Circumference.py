import math

pi = 3.14
def circumference(r):
    return(round(2*pi*r))

radius = float(input("Enter radius in centimeters: "))
print("Circumference is: ", circumference(radius), "centimeters")