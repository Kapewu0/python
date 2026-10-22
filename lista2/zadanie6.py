lista_studentow = ["Kasia","Basia", "Marek", "Darek"]
lista_studentow.append("Józka")
lista_studentow.extend(["Ania","Basia"])
lista_studentow.sort()
print(lista_studentow[3])
print(lista_studentow[:2])
print(lista_studentow[-2:])
while "Basia" in lista_studentow:
    lista_studentow.remove("Basia")
print(lista_studentow, ", ilość studentów: ",len(lista_studentow))
krotka = tuple(lista_studentow)
