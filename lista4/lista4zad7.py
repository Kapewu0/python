# Konrad Marciniak, zadanie nr 7 z listy 4

def parse_if_int(prompt: str) -> int:
    """Deklaracja funkcji mającej na celu sprawdzenie czy użytkownik podał liczbe oraz jej zwrócenie jeśli nią jest,
        jeśli nie to użytkownik otrzymuje komunikat o niepoprawnym wprowadzeniu danych i zostaje poproszony o ponowne wprowadzenie liczby"""
    value = -1
    while value <= 0:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Liczba musi być większa od zera")
                continue
            return value
        except ValueError:
            print("Podano niepoprawną liczbę")
    return value


def main():
    m = parse_if_int("Podaj liczbę wierszy: \t")
    n = parse_if_int("Podaj liczbę kolumn: \t")
    # Stworzenie tablicy elementów iloczynu ich indeksów
    array = [[i * j for j in range(n)] for i in range(m)]
    # Wypisanie tablicy wierszami
    for row in array:
        print(row)

if __name__ == "__main__":
    main()