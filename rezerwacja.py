class Rezerwacja():
    """Klasa umożliwiająca rezerwację seansu."""

    rezerwacje1 = open("rezerwacje_film1.txt", "a")
    rezerwacje2 = open("rezerwacje_film2.txt", "a")
    rezerwacje3 = open("rezerwacje_film3.txt", "a")
    rezerwacje1_lista = []
    rezerwacje2_lista = []
    rezerwacje3_lista = []

    def rezerwowanie_seansu(self, nr_filmu):
        """Rezerwowanie seansu."""

        if nr_filmu == 1:
            while len(self.rezerwacje1_lista) < 5:
                imie = input("podaj imię (q- wyjście): ")
                if imie.lower() != "q":
                    nazwisko = input("podaj nazwisko (q- wyjście): ")
                    if nazwisko.lower() != "q":
                        mail = input("podaj adres e-mail (q- wyjście): ")
                        if mail.lower() != "q":
                            klient = (imie, nazwisko, mail)
                            print(f"Została dokonana rezerwacja"
                                  f" dla {imie.title()}.")
                            self.rezerwacje1_lista.append(klient)
                            self.rezerwacje1.write(
                                f"{len(self.rezerwacje1_lista)}. "
                                f"{imie.title()} {nazwisko.title()}, "
                                f"{mail}.\n")
                else:
                    break

            if len(self.rezerwacje1_lista) >= 5:
                print("Przepraszamy, nie ma już wolnych miejsc na ten film.")

        if nr_filmu == 2:
            while len(self.rezerwacje2_lista) < 5:
                imie = input("podaj imię (q- wyjście): ")
                if imie.lower() != "q":
                    nazwisko = input("podaj nazwisko (q- wyjście): ")
                    if nazwisko.lower() != "q":
                        mail = input("podaj adres e-mail (q- wyjście): ")
                        if mail.lower() != "q":
                            klient = (imie, nazwisko, mail)
                            print(f"Została dokonana rezerwacja"
                                  f" dla {imie.title()}.")
                            self.rezerwacje2_lista.append(klient)
                            self.rezerwacje2.write(
                                f"{len(self.rezerwacje2_lista)}. "
                                f"{imie.title()} {nazwisko.title()}, "
                                f"{mail}.\n")
                else:
                    break

            if len(self.rezerwacje2_lista) >= 5:
                print("Przepraszamy, nie ma już wolnych miejsc na ten film.")

        if nr_filmu == 3:
            while len(self.rezerwacje3_lista) < 5:
                imie = input("podaj imię (q- wyjście): ")
                if imie.lower() != "q":
                    nazwisko = input("podaj nazwisko (q- wyjście): ")
                    if nazwisko.lower() != "q":
                        mail = input("podaj adres e-mail (q- wyjście): ")
                        if mail.lower() != "q":
                            klient = (imie, nazwisko, mail)
                            print(f"Została dokonana rezerwacja"
                                  f" dla {imie.title()}.")
                            self.rezerwacje3_lista.append(klient)
                            self.rezerwacje3.write(
                                f"{len(self.rezerwacje3_lista)}. "
                                f"{imie.title()} {nazwisko.title()}, "
                                f"{mail}.\n")
                else:
                    break

            if len(self.rezerwacje3_lista) >= 5:
                print("Przepraszamy, nie ma już wolnych miejsc na ten film.")

    def zamkniecie_plikow(self):
        """Zamyka pliki."""
        self.rezerwacje1.close()
        self.rezerwacje2.close()
        self.rezerwacje3.close()