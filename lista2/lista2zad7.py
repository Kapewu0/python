# Konrad Marciniak, zadanie nr 7 z listy 2
def sorting_array_with_respect_to_key(list_of_students: list, key: int):
    """Deklaracja funkcji służącej do sortowania elementów zagnieżdżonej tablicy według podanego klucza"""
    for element in list_of_students:
        if len(element) <= key:
            return "Niepoprawny klucz do wybranej tablicy!"
    return sorted(list_of_students, key = lambda item: item[key])


def main():
    list_that_has_to_be_sorted = [(2,8), (5,5), (9,3), (1,0), (3,2), (6,4), (1,9), (10,3), (2,3), (1,7)]
    print(sorting_array_with_respect_to_key(list_that_has_to_be_sorted,1))


if __name__ == "__main__":
    main()