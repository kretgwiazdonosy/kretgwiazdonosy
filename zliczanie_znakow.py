# Plik: Zliczanie_znakow.py

liczba_znakow = 0

while True:
    # Pobranie znaku od użytkownika
    znak = input("Wprowadź znak (wprowadzenie kropki kończy zliczanie): ")

    # Sprawdzenie, czy wprowadzono kropkę
    if znak == ".":
        liczba_znakow += 1
        break

    # Zwiększenie licznika znaków
    liczba_znakow += 1

# Wyświetlenie liczby wprowadzonych znaków
print(f"Liczba wprowadzonych znaków: {liczba_znakow}")  