import math
from math import sqrt


def check_delta():
    a = float(input("Podaj a: \t"))
    b = float(input("Podaj b: \t"))
    c = float(input("Podaj c: \t"))

    if a == 0.0:
        print("Równanie nie jest kwadratowe")
        return

    delta = b**2 - 4*a*c
    match delta:
        case delta if delta == 0.0: print(f"Jeden pierwiastek rzeczywisty: {-b/ (2*a)}")
        case delta if delta > 0.0: print(f"Dwa pierwiastki rzeczywiste: {(-b+sqrt(delta))/(2*a)} oraz {(-b-sqrt(delta))/(2*a)}")
        case _: print(f"Pierwiastki równiania nie są rzeczywiste")
def main():
    check_delta()




main()