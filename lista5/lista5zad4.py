# Konrad Marciniak, zadanie nr 4 z listy 5
def sequences(n, a1 = 1, q = 2):
    """Deklaracja funkcji zwracającej n-ty element ciągu geometrycznego, dla zadanego wyrazu początkowego oraz iloczynu ciągu geometrycznego"""
    return a1*q**(n-1)
def main():
    # Przykładowe użycie funkcji sequences()
    print(sequences(5))
    print(sequences(3, 2))
    print(sequences(5, 2, 10))

if __name__ == "__main__":
    main()