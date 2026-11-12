# Konrad Marciniak, zadanie nr 4 z listy 3
def main():
    # Stworzenie tablicy z elementami będącymi wielokrotnościami liczby 3 mniejszymi od 100
    array = list(range(3, 100, 3))
    print(array)
    # Usunięcie co trzeciego elementu zaczynając od piątego
    del array[4: :3]
    print(array)
    # Średnia arytmetyczna elementów tablicy
    mean = sum(array) / len(array)
    print(mean)


if __name__ == '__main__':
    main()