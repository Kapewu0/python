# Konrad Marciniak, zadanie nr 6 z listy 2
def remove_element_in_array(element: str, array: list):
    """Deklaracja funkcji usuwającej każde wystąpienie wybranego elementu w tablicy"""
    while element in array:
        array.remove(element)


def main():
    list_of_students = ["Kasia", "Basia", "Marek", "Darek"]
    list_of_students.append("Józka")
    list_of_students.extend(["Ania", "Basia"])
    list_of_students.sort()
    print(list_of_students[3])
    print(list_of_students[:2])
    print(list_of_students[-2:])
    # Usunięcie każdego elementu "Basia" w tablicy list_of_students
    remove_element_in_array("Basia", list_of_students)
    print(list_of_students, ", ilość studentów: ", len(list_of_students))
    tuple_from_list_of_students = tuple(list_of_students)
    print(tuple_from_list_of_students)


if __name__ == "__main__":
    main()
