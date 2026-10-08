a, b = 0, 0
while a <= b:
    a = int(input("Podaj większą liczbę "))
    b = int(input("Podaj mniejszą liczbę "))
Z = b % a
Z *= Z + 3
print(Z)