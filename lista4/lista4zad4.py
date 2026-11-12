# Konrad Marciniak, zadanie nr 4 z listy 4
def parse_if_int(prompt: str) -> int:
    """Deklaracja funkcji mającej na celu sprawdzenie czy użytkownik podał liczbe oraz jej zwrócenie jeśli nią jest,
       jeśli nie to użytkownik otrzymuje komunikat o niepoprawnym wprowadzeniu danych i zostaje poproszony o ponowne wprowadzenie liczby"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Podano niepoprawną liczbę")

def main():
    i = parse_if_int("Podaj liczbę przez którą chcesz mnożyć: \n")
    for t in range(1,i+1):
        for j in range(1,11):
            print(j*t, end="\t")
        print("\n")

if __name__ == "__main__":
    main()