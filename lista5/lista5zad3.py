# Konrad Marciniak, zadanie nr 3 z listy 5
import math


def convertion_radians_and_degrees(radians: float|None = None, degrees: float|None = None) -> float | str:
    """Deklaracja funkcji konwertującej radiany na stopnie oraz stopnie na radiany w zalezności od wprowadzonych argumentów"""
    if radians is not None and degrees is not None:
        return "Podano zarówno radiany jak i stopnie"
    elif radians is not None:
        return math.degrees(radians)
    elif degrees is not None:
        return math.radians(degrees)
    else:
        return "Nie podano ani radianów ani stopni!"

def main():
    # Przykładowe użycie funkcji convertion_radians_and_degrees()
    print(convertion_radians_and_degrees(radians=math.pi / 4))
    print(convertion_radians_and_degrees(degrees=90))
    print(convertion_radians_and_degrees(radians=math.pi/2, degrees=90))
    print(convertion_radians_and_degrees())

if __name__ == "__main__":
    main()