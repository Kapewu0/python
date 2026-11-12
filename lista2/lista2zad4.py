# Konrad Marciniak, zadanie nr 4 z listy 2
def change_characters_without_first_one(entry: str, key: str ) -> str:
    """Funkcja sprawdza czy napis został wprowadzony, jeśli nie zostaje wypisany komunikat o błędnym wpisaniu ciągu znaków"""
    if not entry:
        return "Niepoprawny ciąg znaków"
    first_character = entry[0]
    new_entry = first_character
    # Iterowanie przez każdy znak wprowadzonego napisu wraz ze zmianą wszystkich znaków, które to są identyczne z pierwszym znakiem, na wybrany znak ( w tym przypadku został on wywołany z $)
    for i in entry[1:]:
        if i == first_character:
            i = key
        new_entry += i
    return new_entry
def main():
    entry = input("Podaj napis: ")
    print(change_characters_without_first_one(entry, "$"))

if __name__ == "__main__":
    main()