import customtkinter as ctk


okno = ctk.CTk()


def kalkulator():

    def oblicz_wynik():
        dzialanie = wpisz_dzialanie.get()
        if dzialanie == "":
            return
        dzialanie = dzialanie.replace("^", "**")
        try:
            dzialanie = eval(dzialanie)
        except Exception as error:
            print(f"{error = }")
            wpisz_dzialanie.delete(0, ctk.END)
            wpisz_dzialanie.insert(0, "Wpisz poprawnie!")
        else:
            wpisz_dzialanie.delete(0, ctk.END)
            wpisz_dzialanie.insert(0, f"{dzialanie}")

    okno.title("Kalkulator")

    ctk.set_default_color_theme("dark-blue")

    szerokosc = 75
    wysokosc = 50

    wpisz_dzialanie = ctk.CTkEntry(okno, width=300, placeholder_text="Wpisz działanie", font=("Candara", 32))
    wpisz_dzialanie.grid(row=0, column=0, padx=3, pady=10)

    ramka = ctk.CTkFrame(okno)
    ramka.grid(row=1, column=0, sticky="w")

    guzik_wyczysc = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="C", command=lambda: wpisz_dzialanie.delete(0, ctk.END))
    guzik_wyczysc.grid(row=1, column=0, padx=(3, 1), pady=2, sticky="w")

    guzik_7 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="7", command=lambda: wpisz_dzialanie.insert(ctk.END, "7"))
    guzik_7.grid(row=2, column=0, padx=(3, 1), pady=2, sticky="w")

    guzik_4 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="4", command=lambda: wpisz_dzialanie.insert(ctk.END, "4"))
    guzik_4.grid(row=3, column=0, padx=(3, 1), pady=2, sticky="w")

    guzik_1 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="1", command=lambda: wpisz_dzialanie.insert(ctk.END, "1"))
    guzik_1.grid(row=4, column=0, padx=(3, 1), pady=2, sticky="w")

    guzik_kropka = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text=".", command=lambda: wpisz_dzialanie.insert(ctk.END, "."))
    guzik_kropka.grid(row=5, column=0, padx=(3, 1), pady=2, sticky="w")

    guzik_potega = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="^", command=lambda: wpisz_dzialanie.insert(ctk.END, "^"))
    guzik_potega.grid(row=1, column=1, padx=1, pady=2, sticky="w")

    guzik_8 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="8",
                                 command=lambda: wpisz_dzialanie.insert(ctk.END, "8"))
    guzik_8.grid(row=2, column=1, padx=1, pady=2, sticky="w")

    guzik_5 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="5",
                                 command=lambda: wpisz_dzialanie.insert(ctk.END, "5"))
    guzik_5.grid(row=3, column=1, padx=1, pady=2, sticky="w")

    guzik_2 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="2",
                                 command=lambda: wpisz_dzialanie.insert(ctk.END, "2"))
    guzik_2.grid(row=4, column=1, padx=1, pady=2, sticky="w")

    guzik_0 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="0",
                                 command=lambda: wpisz_dzialanie.insert(ctk.END, "0"))
    guzik_0.grid(row=5, column=1, padx=1, pady=2, sticky="w")

    guzik_nawia_o = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="(",
                            command=lambda: wpisz_dzialanie.insert(ctk.END, "("))
    guzik_nawia_o.grid(row=1, column=2, padx=1, pady=2, sticky="w")

    guzik_9 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="9",
                            command=lambda: wpisz_dzialanie.insert(ctk.END, "9"))
    guzik_9.grid(row=2, column=2, padx=1, pady=2, sticky="w")

    guzik_6 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="6",
                            command=lambda: wpisz_dzialanie.insert(ctk.END, "6"))
    guzik_6.grid(row=3, column=2, padx=1, pady=2, sticky="w")

    guzik_3 = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="3",
                            command=lambda: wpisz_dzialanie.insert(ctk.END, "3"))
    guzik_3.grid(row=4, column=2, padx=1, pady=2, sticky="w")

    guzik_rowna_sie = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="=", command=oblicz_wynik)
    guzik_rowna_sie.grid(row=5, column=2, padx=1, pady=2, sticky="w")

    guzik_nawias_z = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text=")",
                            command=lambda: wpisz_dzialanie.insert(ctk.END, ")"))
    guzik_nawias_z.grid(row=1, column=3, padx=(1, 3), pady=2, sticky="w")

    guzik_dzielenie = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="/",
                            command=lambda: wpisz_dzialanie.insert(ctk.END, "/"))
    guzik_dzielenie.grid(row=2, column=3, padx=(1, 3), pady=2, sticky="w")

    guzik_mnozenie = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="*",
                            command=lambda: wpisz_dzialanie.insert(ctk.END, "*"))
    guzik_mnozenie.grid(row=3, column=3, padx=(1, 3), pady=2, sticky="w")

    guzik_odejmowanie = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="-",
                            command=lambda: wpisz_dzialanie.insert(ctk.END, "-"))
    guzik_odejmowanie.grid(row=4, column=3, padx=(1, 3), pady=2, sticky="w")

    guzik_dodawanie = ctk.CTkButton(ramka, width=szerokosc, height=wysokosc, text="+", command=lambda: wpisz_dzialanie.insert(ctk.END, "+"))
    guzik_dodawanie.grid(row=5, column=3, padx=(1, 3), pady=2, sticky="w")


def main():
    kalkulator()
    okno.mainloop()


if __name__ == "__main__":
    main()
