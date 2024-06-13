# Plik: Liczba_punktow.py

# Pobranie liczby punktów zdobytych przez klasę w innych kategoriach
pkt = int(input("Wprowadź liczbę punktów zdobytych przez klasę w innych kategoriach: "))
    
# Pobranie procentu frekwencji
frekwencja = float(input("Wprowadź procent frekwencji: "))
    
# Pobranie średniej ocen
srednia_ocen = float(input("Wprowadź średnią ocen: "))
    
# Sprawdzenie warunków i obliczenie aktualnej liczby punktów
if frekwencja > 94 and srednia_ocen >= 4.0:
    pkt += 20
    
# Wyświetlenie aktualnej liczby punktów
print(f"Aktualna liczba punktów: {pkt}")