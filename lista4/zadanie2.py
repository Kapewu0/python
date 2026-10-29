number = int(input("Podaj liczbę, którą chcesz sprawdzić: \n"))
if number % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")
######################################################
number = int(input("Podaj liczbę, którą chcesz sprawdzić: \n"))
rodzaj = ["parzysta", "nieparzysta"]
print("Liczba jest ", rodzaj[number%2])