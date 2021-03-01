class Repertuar():
    """Klasa przedstawiająca aktualny repertuar wraz z opisami filmów."""

    opis_filmu1 = open("opis_filmu1.txt", encoding="utf8")
    opis_filmu2 = open("opis_filmu2.txt", encoding="utf8")
    opis_filmu3 = open("opis_filmu3.txt", encoding="utf8")

    def wyswietl_repertuar(self):
        """Wyświelenie na ekranie repertuaru."""

        print("REPTERTUAR")
        for tytul in self.opis_filmu1.readlines(1):
            print(f"\t1. {tytul.strip()}")
        for tytul in self.opis_filmu2.readlines(1):
            print(f"\t2. {tytul.strip()}")
        for tytul in self.opis_filmu3.readlines(1):
            print(f"\t3. {tytul.strip()}")

    def wyswietl_opis(self, nr_filmu):
        """Wyświetlenie na ekranie opisu filmu."""

        if nr_filmu == 1:
            for opis in self.opis_filmu1.readlines():
                print(opis.strip())
        elif nr_filmu == 2:
            for opis in self.opis_filmu2.readlines():
                print(opis.strip())
        elif nr_filmu == 3:
            for opis in self.opis_filmu3.readlines():
                print(opis.strip())
        else:
            print("Nie wybrano nr filmu.")

    def zamkniecie_plikow(self):
        """Zamyka pliki."""
        self.opis_filmu1.close()
        self.opis_filmu2.close()
        self.opis_filmu3.close()