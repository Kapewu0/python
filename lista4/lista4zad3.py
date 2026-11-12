# Konrad Marciniak, zadanie nr 3 z listy 4
from math import sqrt


def parse_if_float(prompt: str) -> float:
    """Deklaracja funkcji mającej na celu sprawdzenie czy użytkownik podał liczbe oraz jej zwrócenie jeśli nią jest,
       jeśli nie to użytkownik otrzymuje komunikat o niepoprawnym wprowadzeniu danych i zostaje poproszony o ponowne wprowadzenie liczby"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Podano niepoprawną liczbę")


def get_user_input() -> tuple[float, float, float]:
    """Deklaracja funkcji pobierającej od użytkownika współczynników stojących przy potęgach x w równaniu kwadratowym oraz sprawdzenie czy jest to rzeczywiście równanie kwadratowe,
       funkcja zwraca współczynniki, które to służą do wyznaczenia pierwiastków rzeczywistych w funkcji check_delta()"""
    print("Podaj równanie kwadratowe według wzoru ax² + bx + c")
    a = parse_if_float("Podaj a: \t")
    if a == 0.0:
        print("Równanie nie jest kwadratowe")
        return get_user_input()
    b = parse_if_float("Podaj b: \t")
    c = parse_if_float("Podaj c: \t")
    return a, b, c


def check_delta_and_calculate_real_roots() -> tuple[None, None] | tuple[float, float] | float:
    """Deklaracja funkcji sprawdzającej wartość delty równania kwadratowego oraz zwracającej pierwiastki rzeczywiste tego równania"""
    (a, b, c) = get_user_input()
    delta = b ** 2 - 4 * a * c
    match delta:
        case 0.0:
            return -b / (2 * a)
        case delta if delta > 0.0:
            return (-b + sqrt(delta)) / (2 * a), (-b - sqrt(delta)) / (2 * a)
        case _:
            return None, None


def main():
    # Wypisanie odpowiedniego komunikatu dla obliczonych pierwiastków rzeczywistych
    match check_delta_and_calculate_real_roots():
        case float(x):
            print(f"Jeden pierwiastek rzeczywisty: {x}")
        case float(x1), float(x2):
            print(f"Dwa pierwiastki rzeczywiste: {x1} oraz {x2}")
        case None, None:
            print("Równanie nie posiada pierwiastków rzeczywistych")


if __name__ == "__main__":
    main()
