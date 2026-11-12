# Konrad Marciniak, zadanie nr 5 z listy 3
def main():
    user_input = input("Podaj tekst, który chcesz sprawdzić: \n")
    # Sprawdzenie czy użytkownik podał liczbę naturalną
    if user_input.isdigit():
        print("Podano liczbę naturalną")
    else:
        print("Podany tekst nie zawiera liczby naturalnej")

if __name__ == "__main__":
    main()