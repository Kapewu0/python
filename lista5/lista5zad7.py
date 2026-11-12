# Konrad Marciniak, zadanie nr 7 z listy 5
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

def calculate_factorial(n: int) -> int:
    """Deklaracja funkcji obliczającej silnię z podanej liczby całkowitej"""
    factorial = 1
    if n == 0 or n == 1:
        return 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def main():
    # Przykładowe użycie funkcji calculate_factorial()
    user_input = parse_if_int("Podaj liczbę, której chcesz poznać silnię: ")
    print(f"Silnia liczby {user_input}: ", calculate_factorial(user_input))

if __name__ == "__main__":
    main()