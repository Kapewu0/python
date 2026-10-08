from math import sin, radians

a = float(input("Podaj pierwszy bok: "))
b = float(input("Podaj drugi bok: "))
angle = float(input("Podaj kąt: "))

angle = radians(angle)

area = 0.5 * a * b * sin(angle)
print(area)