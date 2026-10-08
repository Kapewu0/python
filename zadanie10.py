import cmath

first_number = cmath.sin(1j)
print("Część rzeczywista sin(i): ", first_number.real, "Część urojona sin(i): ", first_number.imag)
second_number = cmath.cos(1j)
print("Część rzeczywista cos(i): ", second_number.real, "Część urojona cos(i): ", second_number.imag)
print("sin^2z + cos^2z = ", first_number **2 + second_number **2)