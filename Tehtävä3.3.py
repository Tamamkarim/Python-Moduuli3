
def hemoglobiini_testi():
    # Kysy sukupuoli
    sukupuoli = input("Kirjoita sukupuolesi (mies/nainen): ").lower()

    # Kysy hemoglobiiniarvo
    try:
        hb = int(input("Anna hemoglobiiniarvo (g/l): "))
    except ValueError:
        print("Kirjoita vain numeroita hemoglobiiniarvolle!")
        return
    # Tarkista arvot sukupuolen mukaan
    if sukupuoli == "nainen":
        if hb < 117:
            print("Hemoglobiinisi on liian matala.")
        elif hb > 175:
            print("Hemoglobiinisi on liian korkea.")
        else:
            print("Hemoglobiinisi on normaali.")
    elif sukupuoli == "mies":
        if hb < 134:
            print("Hemoglobiinisi on liian matala.")
        elif hb > 195:
            print("Hemoglobiinisi on liian korkea.")
        else:
            print("Hemoglobiinisi on normaali.")
    else:
        print("Kirjoita sukupuoleksi joko 'mies' tai 'nainen'.")

hemoglobiini_testi()
