# Konrad Marciniak, zadanie nr 2 z listy 3
def main():
    tuple_of_numbers = tuple(range(5))
    tuple_of_numbers += ("pięć", "sześć", "siedem", "osiem", "dziewięć")

    print(*tuple_of_numbers[:3])
    print(*tuple_of_numbers[-2:])
    print(*tuple_of_numbers[1::2])
    print(f"Długość krotki: {len(tuple_of_numbers)}, długość przedostatniego elementu: {len(str(tuple_of_numbers[-2]))}")
    print(tuple_of_numbers[:5] + (5,6) + tuple_of_numbers[-3:])
    print(tuple_of_numbers[:5], (5,6), tuple_of_numbers[-3:])

    tuple_of_numbers += ("",)
# Nie można skorzystać z metody .append() ponieważ krotni są niezmienne, aby dodać element do krotki należy dodać do niej inną krotkę lecz taka operacja modyfikuje pierwszą krotkę a drugą pozostawia bez zmian
if __name__ == "__main__":
    main()