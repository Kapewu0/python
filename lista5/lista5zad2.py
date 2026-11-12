# Konrad Marciniak, zadanie nr 2 z listy 5
def remove_duplicates_from_array(array: list) -> list:
    """Deklaracja fukcji usuwającej duplikaty z podanej tablicy, zwraca skróconą tablicę"""
    return list(dict.fromkeys(array).keys())
def main():
    tab = [1,1,1,2]
    print(remove_duplicates_from_array(tab))


if __name__ == "__main__":
    main()