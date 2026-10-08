import cmath

real = int(input("Podaj część rzeczywistą "))
imaginary = int(input("Podaj część urojoną "))
magnitude = cmath.sqrt(real ** 2 + imaginary ** 2)
argument = cmath.atan(imaginary / real)
conjugate = real+((1j*imaginary).conjugate())
print("Moduł ", magnitude, "Argument: ", argument, "Sprzężenie: ", conjugate)