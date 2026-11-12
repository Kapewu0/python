# Konrad Marciniak, zadanie nr 2 z listy 4
def parse_if_int(prompt: str) -> int:
    """Deklaracja funkcji mającej na celu sprawdzenie czy użytkownik podał liczbe oraz jej zwrócenie jeśli nią jest,
       jeśli nie to użytkownik otrzymuje komunikat o niepoprawnym wprowadzeniu danych i zostaje poproszony o ponowne wprowadzenie liczby"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Podano niepoprawną liczbę")
def main():
    number = parse_if_int("Podaj liczbę, którą chcesz sprawdzić: \n")
    if number % 2 == 0:
        print("Liczba jest parzysta")
    else:
        print("Liczba jest nieparzysta")
    ######################################################
    # Wersja bez użycia instrukcji if
    number = parse_if_int("Podaj liczbę, którą chcesz sprawdzić: \n")
    rodzaj = ["parzysta", "nieparzysta"]
    print("Liczba jest ", rodzaj[number%2])