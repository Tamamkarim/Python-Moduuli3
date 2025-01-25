
def tarkista_karkausvuosi():
    # Kysy vuosi
    try:
        vuosi = float(input("Anna vuosiluku: "))
    except ValueError:
        print("Kirjoita vain numeroita!")
        return

    if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
        print(f"{vuosi} on karkausvuosi!")
    else:
        print(f"{vuosi} ei ole karkausvuosi.")

tarkista_karkausvuosi()

