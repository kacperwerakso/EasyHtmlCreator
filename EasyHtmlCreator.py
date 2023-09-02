class Menu:
    @staticmethod
    def menu():
        print("\n----- WITAJ W EasyHtmlCreator -----\n")
        wybor = input("\n0. Wyjście\n1. Utwórz stronę\n")
        if wybor == "1":
            Wpisz().wpisywanie()
        elif wybor == "0":
            pass
        else:
            return Menu().menu()

class Wpisz:
    @staticmethod
    def wpisywanie():
        print("\n----- POMYŚLNIE ROZPOCZĘTO TWORZENIE STRONY -----\n\n")
        naglowek = input("Wprowadź treść nagłówka na stronie: ")
        kolor_naglowek = input("Wybierz kolor nagłówka (j. ang): ")
        tresc = input("Wprowadź treść pod nagłówkiem: ")
        kolor_tresc = input("Wybierz kolor treści (j. ang): ")
        tlo = input("Wybierz tło strony (j. ang): ")
        nazwa = input("Nazwa pliku przechowującego stronę: ")
        Pelna_nazwa = open(f"{nazwa}.html", "w")
        Pelna_nazwa.write(f"<html>\n<head>\n<title>Tresc do HTML</title>\n</head> <body bgcolor={tlo}> <h1><font color={kolor_naglowek}><center><br><br>{naglowek}</center></font></h1>\n<center><p><br><br><font color={kolor_tresc}>{tresc}</font></p></center>\n</body></html>")
        Pelna_nazwa.close()
        ostatnie = input("\n----- POMYŚLNIE UKOŃCZONO TWORZENIE STRONY -----\n\nPlik znajduje się w folderze EasyHtmlCreator\n\n0. Wyjście\n1. Wróc do początku\n")
        if ostatnie == "1":
            return Menu().menu()
        elif ostatnie == "0":
            pass
        else:
            return Menu().menu()

o = Menu()
o.menu()