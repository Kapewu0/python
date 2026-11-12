# Konrad Marciniak, zadanie nr 6 z listy 3

def main():
    user_input = input("Podaj sekwencję liczb całkowitych oddzielonych przecinkiem: \n")
    strings = user_input.split(",")
    # Próba konwersji elementów tablicy strings na zmienne typu int, jeśli użytkownik nie poda liczb całkowitych zostaje poproszony o ponowne wprowadzenie liczb
    try:
        numbers = [int(x) for x in strings]
    except ValueError:
        print("Podano niepoprawną liczbę")
        return main()

    equation = " + ".join(str(x) for x in numbers)
    print(equation, " = ", sum(numbers))
    return None


if __name__ == "__main__":
    main()