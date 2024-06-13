# Plik: Romb.py

import math

def main():
    try:
        # Pobranie sumy długości przekątnych
        D = float(input("Wprowadź sumę długości przekątnych: "))
        
        # Pobranie długości jednego boku
        a = float(input("Wprowadź długość jednego boku: "))
    except ValueError:
        print("Wprowadzone dane nie są liczbami. Uruchom program ponownie i wprowadź poprawne dane.")
        return
    
    # Sprawdzenie poprawności danych wejściowych
    if D <= 2 * a:
        print("Błędne dane: suma długości przekątnych musi być większa niż 2 * długość boku.")
        return
    
    # Obliczenie długości przekątnych
    # Rozwiązanie układu równań:
    # 1. d1 + d2 = D
    # 2. sqrt((d1/2)^2 + (d2/2)^2) = a
    # Po podstawieniu d2 = D - d1 i rozwiązaniu równania kwadratowego na d1
    A = 1
    B = -D
    C = (D**2 / 4) - (a**2)
    
    delta = B**2 - 4 * A * C
    
    if delta < 0:
        print("Błędne dane: brak rozwiązań dla podanych wartości.")
        return
    
    d1 = (-B + math.sqrt(delta)) / (2 * A)
    d2 = D - d1
    
    print(f"Długości przekątnych: d1 = {d1}, d2 = {d2}")

# Wywołanie funkcji głównej
if __name__ == "__main__":
    main()