# Konrad Marciniak, zadanie nr 2 z listy 1
# Zaimportowanie biblioteki math, która posiada funkcję sinus(przyjmującej radiany jako argument) oraz konwersję stopni na radiany
import math
def triangle_area(first_side = 0.0, second_side = 0.0, given_angle = 90.0) -> float:
    """Deklaracja funkcji wyliczającej pole trójkąta, domyślne wartości uwzględniają brak podania jednego z boków lub brak podania kąta"""
    return 0.5 * first_side * second_side * math.sin(math.radians(given_angle))
def main():
    # Przypisanie wartości do odpowiednich zmiennych
    a = 3
    b = 4
    angle = 47
    # Wypisanie pola trójkąta dla wybranych wartości
    print(triangle_area(a, b, angle))

if __name__ == "__main__":
    main()

