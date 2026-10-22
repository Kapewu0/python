listOfStudents = ["Kasia", "Basia", "Marek", "Darek"]
listOfStudents.append("Józka")
listOfStudents.extend(["Ania", "Basia"])
listOfStudents.sort()
print(listOfStudents)
print(listOfStudents[3])
print(listOfStudents[:2])
print(listOfStudents[-2:])
while "Basia" in listOfStudents:
    listOfStudents.remove("Basia")
print(listOfStudents)
print("ilość studentów: ", len(listOfStudents))

studentTuple = tuple(listOfStudents)
print(studentTuple)