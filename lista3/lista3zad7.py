# Konrad Marciniak, zadanie nr 7 z listy 3
import random
import string
def parse_if_int(prompt: str) -> int:
    """Deklaracja funkcji mającej na celu sprawdzenie czy użytkownik podał liczbe oraz jej zwrócenie jeśli nią jest,
       jeśli nie to użytkownik otrzymuje komunikat o niepoprawnym wprowadzeniu danych i zostaje poproszony o ponowne wprowadzenie liczby"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Podano niepoprawną liczbę")
def main():
    number = parse_if_int("Podaj liczbę kluczy: \n")
    # Stworzenie listy znaków jakie można otrzymać, litery oraz cyfry
    characters = string.ascii_letters + string.digits
    # Stworzenie słownika o "losowych" wartościach dla podanej ilości kluczy
    dictionary = {k: random.choice(characters) for k in range(1, number + 1)}
    print(dictionary)

if __name__ == "__main__":
    main()