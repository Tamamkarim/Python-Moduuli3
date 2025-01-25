
def onko_karkausvuosi(vuosi):
    if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
        return True
    else:
        return False

vuosi = int(input("vuosiluku: "))

if onko_karkausvuosi(vuosi):
    print(f"{vuosi} on karkausvuosi.")
else:
    print(f"{vuosi} ei ole karkausvuosi.")
