class Repertuar():
    """Klasa przedstawiająca aktualny repertuar wraz z opisami filmów."""

    def wyswietl_repertuar(self):
        """Wyświelenie na ekranie repertuaru."""

        opis_filmu1 = open("opis_filmu1.txt", encoding="utf8")
        opis_filmu2 = open("opis_filmu2.txt", encoding="utf8")
        opis_filmu3 = open("opis_filmu3.txt", encoding="utf8")

        print("REPTERTUAR")
        for tytul in opis_filmu1.readlines(1):
            print(f"\t1. {tytul.strip()}")
        for tytul in opis_filmu2.readlines(1):
            print(f"\t2. {tytul.strip()}")
        for tytul in opis_filmu3.readlines(1):
            print(f"\t3. {tytul.strip()}")

        opis_filmu1.close()
        opis_filmu2.close()
        opis_filmu3.close()

    def wyswietl_opis(self, nr_filmu):
        """Wyświetlenie na ekranie opisu filmu."""

        opis_filmu1 = open("opis_filmu1.txt", encoding="utf8")
        opis_filmu2 = open("opis_filmu2.txt", encoding="utf8")
        opis_filmu3 = open("opis_filmu3.txt", encoding="utf8")

        if nr_filmu == 1:
            for opis in opis_filmu1.readlines():
                print(opis.strip())
        elif nr_filmu == 2:
            for opis in opis_filmu2.readlines():
                print(opis.strip())
        elif nr_filmu == 3:
            for opis in opis_filmu3.readlines():
                print(opis.strip())
        else:
            print("Nie wybrano nr filmu.")

        opis_filmu1.close()
        opis_filmu2.close()
        opis_filmu3.close()