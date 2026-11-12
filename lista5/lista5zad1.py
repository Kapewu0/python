# Konrad Marciniak, zadanie nr 1 z listy 5
def main():
    # Pobranie od użytkownika ciągu znaków, usunięcie spacji, tabulatorów oraz rozdzielenie znaków względem przecinków
    text = input("Podaj tablicę (liczby oddzielone przecinkiem): \n").strip().split(",")
    # Próba konwersji elementów tablicy na typ int, w przypadku błędu program informuje o błędzie i ponawia wprowadzanie tablicy
    try:
        array = [int(x) for x in text]
    except ValueError:
        print("Podano niepoprawną liczbę")
        return main()
    # Deklaracja sumy elementów tablicy oraz ich iloczynu
    sum_of_elements = sum(array)
    multiplication = 1
    for i in array:
        multiplication *= i
    print("Suma: ", sum_of_elements)
    print("Iloczyn: ", multiplication)
    return None


if __name__ == "__main__":
    main()