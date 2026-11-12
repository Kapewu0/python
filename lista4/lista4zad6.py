# Konrad Marciniak, zadanie nr 6 z listy 4
def main():
    # Wypisanie trójkąta z liczb od 1 do 7
    for n in range(1,8):
        print(*[n]*n, sep="")

if __name__ == "__main__":
    main()