# Konrad Marciniak, zadanie nr 10 z listy 1
import cmath

def main():
    z = 1j
    sinus = cmath.sin(z)
    cosinus = cmath.cos(z)
    # Wypisanie poszczególnych elementów liczb zespolonych
    print("Re sin(i) = ", sinus.real)
    print("Im sin(i) = ", sinus.imag)
    print("Re cos(i) = ", cosinus.real)
    print("Im cos(i) = ", cosinus.imag)
    # Zapisanie "jedynki" trygonometrycznej
    square_sum = sinus**2 + cosinus**2
    # Otrzymujemy wartość zbliżoną do 1 wraz z błędem ograniczenia dokładności zmiennych typu float
    print("sin²(i) + cos²(i) = ", square_sum)
    print("Czy jest to 1? : ", cmath.isclose(square_sum, 1))
if __name__ == "__main__":
    main()