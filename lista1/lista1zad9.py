# Konrad Marciniak, zadanie nr 9 z listy 1
import cmath
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
    a = parse_if_float("Podaj realis liczby zespolonej: ")
    b = parse_if_float("Podaj imaginalis liczby zespolonej: ")
    return a, b


def main():
    (a, b) = user_input()
    z = complex(a, b)
    print("Moduł |z|: ", abs(z))
    print("Argument z: ", cmath.phase(z))
    print("Sprzężenie z: ", z.conjugate())

if __name__ == "__main__":
    main()
