# Konrad Marciniak, zadanie nr 1 z listy 2
def main():
    # Wypisanie elementów listy, poprzez jej rozpakowanie, które są oddzielone ;
    print(*[1.2e3 + 34.5]*20, sep="; ")

if __name__ == "__main__":
    main()