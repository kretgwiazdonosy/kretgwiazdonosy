# Plik: Grupy.py

# Pobranie liczby punktów z testu
punkty = float(input("Wprowadź liczbę punktów uzyskanych z testu (w procentach): "))
    
# Pobranie oceny z języka na świadectwie ukończenia szkoły podstawowej
ocena = int(input("Wprowadź ocenę z języka na świadectwie ukończenia szkoły podstawowej: "))
    
# Sprawdzenie kwalifikacji do grupy
if punkty > 90 or ocena >= 5:
    print("Grupa zaawansowana.")
else:
    print("Grupa podstawowa.")
