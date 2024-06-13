# Plik: Podzielne_przez_3.py

licznik = 0
    
while True:
    try:
        # Pobranie liczby od użytkownika
        liczba = int(input("Wprowadź liczbę całkowitą (0 aby zakończyć): "))
    except ValueError:
        print("To nie jest liczba całkowita. Spróbuj ponownie.")
        continue

    # Sprawdzenie, czy liczba to zero
    if liczba == 0:
        break

    # Sprawdzenie podzielności przez 3
    if liczba % 3 == 0:
        licznik += 1

# Wyświetlenie liczby liczb podzielnych przez 3
print(f"Liczba liczb podzielnych przez 3: {licznik}")