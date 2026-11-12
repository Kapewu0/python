# Konrad Marciniak, zadanie nr 1 z listy 4
def get_users_input_first_character() -> str:
    """Deklaracja funkcji pobierającej od użytkownika ciąg znaków, oraz zwrócenie jego pierwszego znaku, w przypadku nie podania ciągu znaków użytkownik proszony jest o ponowne wprowadzenie znaków
       Ponadto pierwszy znak zostaje zwrócony jako mała litera w celu uproszczenia dalszych porównań"""
    while True:
        try:
            return input("Podaj literę którą chcesz sprawdzić: \n")[0].lower()
        except IndexError:
            print("Nie podano litery, spróbuj ponownie")
def main():
    letter = get_users_input_first_character()
    # Tablice samogłosek oraz spółgłosek
    vowels = ["a", "e", "i", "o", "u","y", "ą", "ę", "ó"]
    consonants = ["b", "c", "ć", "d", "f", "g", "h", "j", "k", "l", "ł", "m", "n", "ń", "p", "r", "s", "ś", "t", "w", "z", "ź", "ż"]
    if letter in vowels:
        print("Podana litera jest samogłoską")
    elif letter in consonants:
        print("Podana litera jest spółgłoską")
    else:
        print("Podany znak nie jest ani samogłoską ani spółgłoską")

if __name__ == "__main__":
    main()