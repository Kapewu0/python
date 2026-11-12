import math


def convertion_radians_and_degrees(radians = None, degrees = None):
    if radians != None and degrees != None:
        print("Podano zarówno radiany jak i stopnie")
        return
    elif radians != None:
       return math.degrees(radians)
    elif degrees != None:
        return math.radians(degrees)
    else:
        print("Nie podano ani radianów ani stopni!")
        return
print(convertion_radians_and_degrees(radians = math.pi / 4))
print(convertion_radians_and_degrees(degrees = 90))
