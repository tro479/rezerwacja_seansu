from repertuar import Repertuar

aktualne_filmy = Repertuar()

while True:

    print()
    print("0- Wyświetl repertuar.")
    print("1- Zobacz opis filmu nr 1.")
    print("2- Zobacz opis filmu nr 2.")
    print("3- Zobacz opis filmu nr 3.")
    print("4- Przejdź do rezerwacji.")
    print("5- Wyjście.")
    print()

    wybor_uzytkownika = int(input("Wybierz opcję: "))

    if wybor_uzytkownika == 0:
        aktualne_filmy.wyswietl_repertuar()
    elif wybor_uzytkownika == 1:
        aktualne_filmy.wyswietl_opis(1)
    elif wybor_uzytkownika == 2:
        aktualne_filmy.wyswietl_opis(2)
    elif wybor_uzytkownika == 3:
        aktualne_filmy.wyswietl_opis(3)
    elif wybor_uzytkownika == 4:
        print("Trwają pracę nad tą częścią kodu.")
    elif wybor_uzytkownika == 5:
        break
    else:
        print("Nie wybrano żadnej dostępnej opcji.")
