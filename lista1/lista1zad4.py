# Konrad Marciniak, zadanie nr 4 z listy 1
import builtins
def main():
    print(dir(builtins))
    help(print)
    print("\"Ala ma kota\"")
    print(2 + 2)
    print(2 ** 5,  35 // 2,  35 / 2, 35 % 2, sep="\t")
    print(2 ** 5,  35 // 2,  35 / 2, 35 % 2, sep="\n")
if __name__ == "__main__":
    main()