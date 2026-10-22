entry = input("Podaj napis: ")
first_character = entry[0]
new_entry = first_character
for i in entry[1:]:
    if i == first_character:
        i = "$"
    new_entry += i

print(new_entry)
