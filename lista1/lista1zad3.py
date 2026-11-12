# Konrad Marciniak, zadanie nr 3 z listy 1
# Zaimportowanie biblioteki math, która posiada funkcję sinus(przyjmującej radiany jako argument) oraz konwersję stopni na radiany
import math



def triangle_area(first_side= 0.0, second_side= 0.0, given_angle= 90.0) -> float:
    """Deklaracja funkcji wyliczającej pole trójkąta, reszta z dzielenia przez 180 w celu uniknięcia ujemnego pola"""
    return 0.5 * first_side.__abs__() * second_side.__abs__() * math.sin(math.radians(given_angle % 180))



def parse_if_float(prompt: str) -> float:
    """Deklaracja funkcji mającej na celu sprawdzenie czy użytkownik podał liczbe oraz jej zwrócenie jeśli nią jest,
       jeśli nie to użytkownik otrzymuje komunikat o niepoprawnym wprowadzeniu danych i zostaje poproszony o ponowne wprowadzenie liczby"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Podano niepoprawną liczbę")


def user_input() -> tuple[float, float, float]:
    """Deklaracja funkcji, która pobiera od użytkownika wartości i zwraca je jeśli są one liczbami"""
    first_side = parse_if_float("Podaj pierwszy bok trójkąta: ")
    second_side = parse_if_float("Podaj drugi bok trójkąta: ")
    given_angle = parse_if_float("Podaj kąt trójkąt między bokami: ")
    return first_side, second_side, given_angle


def main():
    (a, b, angle) = user_input()
    print(triangle_area(a, b, angle))


if __name__ == "__main__":
    main()
