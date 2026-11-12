# Konrad Marciniak, zadanie nr 3 z listy 2
def main():
    entry = input("Podaj napis z którego chcesz stworzyć nowy napis: ")
    print(entry[:2] + entry[-2:])


if __name__ == "__main__":
    main()