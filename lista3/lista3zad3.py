# Konrad Marciniak, zadanie nr 3 z listy 3

def main():
    slubowanie ="""
    wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
    - zdobywac wiedzę i umiejętności,
    - postepować zgodnie z prawe, tradycją i dobrymi obyczajami akademickimi,
    - dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
    """
    slubowanie = slubowanie[0].capitalize() + slubowanie[1:]
    amount_of_i_characters = slubowanie.count("i")
    amount_of_i_conjunction = slubowanie.count(" i ")
    print(f"Ilość liter 'i' w tekście: {amount_of_i_characters}")
    print(f"Ilość spójnika 'i' w tekście: {amount_of_i_conjunction}")
    print("Czy występuje słowo \"Uniwersytet\"?: ", "Uniwersytet" in slubowanie)
    words = slubowanie.split()
    words = [s for s in words if s != "-"]
    print("Ilość słów: ", len(words))
    lines = slubowanie.strip().split("\n")
    print("Ilość linii: ", len(lines))

if __name__ == "__main__":
    main()