# Konrad Marciniak, zadanie nr 2 z listy 2
def main():
    entry = input("Podaj napis, który ma zostać wypisany 30-krotnie: \n")
    print(*[entry] * 30, sep='\n')


if __name__ == "__main__":
    main()