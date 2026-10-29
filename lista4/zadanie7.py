m = int(input("Podaj liczbę wierszy: \t"))
n = int(input("Podaj liczbę kolumn: \t"))
for i in range(1, m+1):
    for j in range(1, n+1):
        print(i*j, end="\t")
    print("\n")