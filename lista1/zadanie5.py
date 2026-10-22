outer = input("Podaj napis: ")
inner = input("Podaj napis do wstawienia: ")
output = outer[:len(outer)//2] + inner + outer[len(outer)//2:]
print(output)
