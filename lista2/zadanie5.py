entry = input("Podaj napis: ")
parenthesis = input("Podaj nawiasy: ")
(firstHalf, secondHalf) = (parenthesis[:len(parenthesis)//2], parenthesis[len(parenthesis)//2:])
new_entry = firstHalf + entry + secondHalf
print(new_entry)
