# Konrad Marciniak, zadanie nr 9 z listy 2
from itertools import chain
def main():
    array = [[2,4,3], [1,5,6],[9],[7,9,0]]
    # Stworzenie listy z iteratora tablicy array
    result = list(chain.from_iterable(array))
    print(result)


if __name__ == "__main__":
    main()