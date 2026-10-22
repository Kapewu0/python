import random
import string
number = int(input("Podaj liczbę kluczy: \n"))
znaki = string.ascii_letters + string.digits
slownik = {k: random.choice(znaki) for k in range(1, number + 1)}
print(slownik)