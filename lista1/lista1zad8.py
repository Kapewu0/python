# Konrad Marciniak, zadanie nr 8 z listy 1

def parse_if_float(prompt: str) -> float:
    """Deklaracja funkcji mającej na celu sprawdzenie czy użytkownik podał liczbe oraz jej zwrócenie jeśli nią jest,
       jeśli nie to użytkownik otrzymuje komunikat o niepoprawnym wprowadzeniu danych i zostaje poproszony o ponowne wprowadzenie liczby"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Podano niepoprawną liczbę")


def user_input() -> tuple[float, float]:
    """Deklaracja funkcji, która pobiera od użytkownika wartości i zwraca je jeśli są one liczbami"""
    a = parse_if_float("Podaj pierwszą liczbę: ")
    b = parse_if_float("Podaj drugą liczbę (mniejszą od pierwszej): ")
    while b >= a:
        print("Druga liczba musi być mniejsza od pierwszej! Spróbuj ponownie")
        b = parse_if_float("Podaj drugą liczbę (mniejszą od pierwszej): ")
    return a, b


def main():
    (a, b) = user_input()
    z = b % a
    z *= z + 3
    print(z)


if __name__ == "__main__":
    main()
