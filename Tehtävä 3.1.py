import math

pituus = float(input("Anna kuhan pituus cm: "))

if pituus < 37:
    puuttuu = 37 - pituus
    print("Laske kuha .")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} s.")