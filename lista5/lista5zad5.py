# Konrad Marciniak, zadanie nr 5 z listy 5
def calculate_factorial(n: int) -> int:
    """Deklaracja funkcji obliczającej silnię z podanej liczby całkowitej"""
    factorial = 1
    if n == 0 or n == 1:
        return 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
def print_pascal_triangle(n: int):
    """Deklaracja funkcji wypisującej n wierszy trójkąta Pascala"""
    for i in range(n):
        print(" " * (n - i), end="")

        for j in range(i + 1):
            value = calculate_factorial(i) // (calculate_factorial(j) * calculate_factorial(i-j))
            print(value, end=" ")
        print()

def main():
    # Przykładowe użycie funkcji print_pascal_triangle()
    print_pascal_triangle(5)


if __name__ == "__main__":
    main()