lista = list(range(3,100,3))
del lista[4::3]
srednia = sum(lista) / len(lista)
print(lista)
print(srednia)