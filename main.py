from pojistenec import Pojistenec

def pridatUzivatele():
    # prida uzivatele na seznam pojistenci
    jmeno = input("Zadej jmeno pojistence: ")
    prijmeni = input("Zadej prijmeni pojistence: ")
    vek = input("Zadej vek pojistence: ")
    telefon = input("Zadej telefon pojistence: ")

    novyPojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
    pojistenci.append(novyPojistenec)

    return "\n--- uspesne pridani noveho pojistence ---\n"

def hledatUzivatele():
    # vyhleda uzivatele v seznamu pojistenci
    hledaneJmeno = input("Zadej jmeno HLEDANEHO pojistence: ")
    hledanePrijmeni = input("Zadej prijmeni HLEDANEHO pojistence: ")

    for item in pojistenci:
        if item.jmeno == hledaneJmeno and item.prijmeni == hledanePrijmeni:
            print("Hledany pojistenec je: ", item.jmeno, item.prijmeni, item.vek, item.telefon, "\n")
            return
    print("!!! Takovy pojistenec neni v databazi !!!")

pojistenci = []

if __name__ == "__main__":
    while True:
        print("--------------------")
        print("Evidence pojistenych")
        print("--------------------\n")

        print("Vyberte si akci")
        print("1 - Pridat noveho pojisteneho")
        print("2 - Vypsat vsechny pojistene")
        print("3 - Hledani pojistence")
        print("4 - Konec")
        akce = input()

        if akce == "1":
            print(pridatUzivatele())
        elif akce == "2":
            for item in pojistenci:
                print(item.jmeno,item.prijmeni,item.vek,item.telefon)
        elif akce == "3":
            hledatUzivatele()
        elif akce == "4":
            print("Konec aplikace")
            break
        else:
            print("Neplatna hodnota\n")


