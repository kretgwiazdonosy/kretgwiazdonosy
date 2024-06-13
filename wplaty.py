# wpłaty.py

try: 
  kwota = float(input("Podaj potrzebna kwote: "))
  suma_wplat = 0

except ValueError:
  print("wprowadzono błędną wartość")
  quit()

while suma_wplat < kwota:
  
  try:
    wplata = float(input("Wprowadz wplate: "))
  
    suma_wplat += wplata
      
    print(f"Kwota zebrana: {suma_wplat} zl")


  except:
    print("wprowadzono błędną wartoś")
    pass

print(f"Nadplata: {suma_wplat - kwota} zl")
input("\n\nAby zakonczyc, nacisnij Enter:")