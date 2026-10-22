user_input = input("Podaj sekwencję liczb całkowitych oddzielonych przecinkiem: \n")
strings = user_input.split(",")
numbers = [int (x) for x in strings]
dzialanie = " + ".join(str(x) for x in numbers)
print(dzialanie, " = ", sum(numbers))