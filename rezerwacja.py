class Rezerwacja():
    """Klasa umożliwiająca rezerwację seansu."""

    rezerwacje1 = open("rezerwacje_film1.txt", "w")
    rezerwacje2 = open("rezerwacje_film2.txt", "w")
    rezerwacje3 = open("rezerwacje_film3.txt", "w")

    def rezerwowanie_seansu(self, nr_filmu):
        """Rezerwowanie seansu."""

        if nr_filmu == 1:
            rezerwacje1_lista = []

            while len(rezerwacje1_lista) < 5:
                imie = input("podaj imię (q- wyjście): ")
                if imie.lower() != "q":
                    nazwisko = input("podaj nazwisko (q- wyjście): ")
                    if nazwisko.lower() != "q":
                        mail = input("podaj adres e-mail (q- wyjście): ")
                        if mail.lower() != "q":
                            klient = (imie, nazwisko, mail)
                            print(f"Została dokonana rezerwacja"
                                  f" dla {imie.title()}.")
                            rezerwacje1_lista.append(klient)
                            self.rezerwacje1.write(
                                f"{len(rezerwacje1_lista)}. {imie.title()} "
                                f"{nazwisko.title()}, {mail}.\n")
                else:
                    break

            if len(rezerwacje1_lista) >= 5:
                print("Przepraszamy, nie ma już wolnych miejsc na ten film.")

aaa = Rezerwacja()
aaa.rezerwowanie_seansu(1)