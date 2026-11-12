# Konrad Marciniak, zadanie nr 6 z listy 5
def sum_of_n_harmonic_series_numbers(n: int) -> float:
    """Deklaracja funkcji sumującej n wyrazów szeregu harmonicznego"""
    sum_of_harmonic_series = 0
    for i in range(1, n + 1):
        sum_of_harmonic_series += 1 / i
    return sum_of_harmonic_series

def main():
    # Przykładowe użycie funkcji sum_of_n_harmonic_series_numbers()
    print(sum_of_n_harmonic_series_numbers(100))


if __name__ == "__main__":
    main()