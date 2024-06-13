# Plik: Rownanie_kwadratowe.py

import math

def main():
    try:
        # Pobranie współczynników od użytkownika
        a = float(input("Wprowadź współczynnik a: "))
        b = float(input("Wprowadź współczynnik b: "))
        c = float(input("Wprowadź współczynnik c: "))
    except ValueError:
        print("Wprowadzone dane nie są liczbami. Uruchom program ponownie i wprowadź poprawne dane.")
        return

    # Sprawdzenie poprawności współczynnika a
    if a == 0:
        print("Błędne dane: współczynnik a nie może być równy 0.")
        return

    # Obliczenie delty
    delta = b**2 - 4*a*c

    # Wyznaczenie pierwiastków równania
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Pierwiastki równania: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Równanie ma jeden pierwiastek podwójny: x = {x}")
    else:
        print("Równanie nie ma pierwiastków rzeczywistych.")

# Wywołanie funkcji głównej
if __name__ == "__main__":
    main()