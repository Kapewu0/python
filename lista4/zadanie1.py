letter = input("Podaj literę którą chcesz sprawdzić: \n")[0].lower()
vowels = ["a", "e", "i", "o", "u","y", "ą", "ę", "ó"]
if letter in vowels:
    print("Podana litera jest samogłoską")
else:
    print("Podana litera jest spółgłoską")