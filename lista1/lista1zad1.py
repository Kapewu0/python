# Konrad Marciniak, zadanie nr 1 z listy 1
def main():
    # Wczytanie od użytkownika pierwszego ciągu znaków
    a = input("Podaj pierwszy napis: ")
    # Wczytanie od użytkownika drugiego ciągu znaków
    b = input("Podaj drugi napis: ")
    # Konkatenacja ciągów znaków
    suma = a + b
    # Wypisanie połączonych ciągów znaków
    print(suma)
    # Funkcja input() zwraca podany przez użytkownika ciąg znaków (typ zmiennej to string) więc łatwo domyśleć się, iż dodanie dwóch ciągów znaków zwróci nam ciąg znaków
    # W celu osiągnięcia działającego "kalkulatora", służącego do dodawania dwóch liczb należy konwertować podany przez użytkownika ciąg znaków na int lub float w następujący sposób:
    # a = int(input("Podaj liczbę: ))
    # lub
    # a = float(input("Podaj liczbę: "))
if __name__ == "__main__":
    main()