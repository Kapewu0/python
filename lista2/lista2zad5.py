# Konrad Marciniak, zadanie nr 5 z listy 2
def main():
    entry = input("Podaj napis: ")
    parenthesis = input("Podaj nawiasy: ")
    # Rozdzielenie zmiennej parenthesis po środku w celu późniejszego wprowadzenia napisu pomiędzy
    (firstHalf, secondHalf) = (parenthesis[:len(parenthesis)//2], parenthesis[len(parenthesis)//2:])
    new_entry = firstHalf + entry + secondHalf
    print(new_entry)


if __name__ == "__main__":
    main()