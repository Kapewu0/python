i = int(input("Podaj liczbę przez którą chcesz mnożyć: \n"))
for t in range(1,i+1):
    for n in range(1,11):
        print(n*t, end="\t")
    print("\n")