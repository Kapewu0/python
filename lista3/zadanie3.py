from itertools import count


slubowanie ="""
wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
- zdobywac wiedzę i umiejętności,
- postepować zgodnie z prawe, tradycją i dobrymi obyczajami akademickimi,
- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
"""
nowe_slubowanie = slubowanie[0].capitalize() + slubowanie[1:]
amount_of_i_1 = nowe_slubowanie.count("i")
amount_of_i_2 = nowe_slubowanie.count(" i ")
print(f"Ilość liter 'i' w tekście: {amount_of_i_1}")
print(f"Ilość spójnika 'i' w tekście: {amount_of_i_2}")
print("Uniwersytet" in slubowanie)
slowa = slubowanie.split()
slowa = [s for s in slowa if s != "-"]
print("Ilość słów: ", len(slowa))
linie = slubowanie.strip().split("\n")
print("Ilość linii: ", len(linie))