# Konrad Marciniak, zadanie nr 5 z listy 4
def parse_if_int(prompt: str) -> int:
    """Deklaracja funkcji mającej na celu sprawdzenie czy użytkownik podał liczbe oraz jej zwrócenie jeśli nią jest,
       jeśli nie to użytkownik otrzymuje komunikat o niepoprawnym wprowadzeniu danych i zostaje poproszony o ponowne wprowadzenie liczby"""
    value = -1
    while value < 0:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Liczba nie może być ujemna")
                continue
        except ValueError:
            print("Podano niepoprawną liczbę")
            continue
    return value


def print_fibonacci_sequence(n: int):
    """Deklaracja funkcji wypisującej kolejne liczby ciągu Fibonnaciego z górną granicą podaną przez użytkownika"""
    previous = 0
    current = 1
    while previous <= n:
        print(previous)
        previous, current = current, previous + current

def main():
    print_fibonacci_sequence(parse_if_int("Podaj górną granicę szeregu Fibonacciego: \n"))


if __name__ == "__main__":
    main()