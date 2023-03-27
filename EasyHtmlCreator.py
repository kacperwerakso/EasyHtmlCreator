class Menu:
    @staticmethod
    def menu():
        print("\n----- WITAJ W EasyHtmlCreator -----\n")
        wybor = input("\n0. Wyjście\n1. Utwórz strone\n")
        if wybor == "1":
            print(Wpisz().wpisywanie())
        elif wybor == "0":
            pass
        else:
            return Menu().menu()

class Wpisz:
    @staticmethod
    def wpisywanie():
        print("\n----- POMYŚLNIE ROZPOCZĘTO TWORZENIE STRONY -----\n\n")
        naglowek = input("Wprowadź treść nagłówka na stronie: ")
        kolor_naglowek = input("Wybierz kolor nagłówka(j.ang): ")
        tresc = input("Wprowadź treść pod nagłówkiem: ")
        kolor_tresc = input("Wybierz kolor treści(j.ang): ")
        tlo = input("Wybierz tło strony(j.ang): ")
        nazwa = input("Nazwa pliku przechowującego stronę: ")
        Pelna_nazwa = (open(f"EasyHtmlCreator/{nazwa}.html","w"))
        Pelna_nazwa.write(f"<html>\n<head>\n<title> \nTresc do HTML\n \
           </title>\n</head> <body bgcolor={tlo}> <h1>\
           <font color = {kolor_naglowek}><center>{naglowek}</center></font></h1>\n \
           <h2><font color = {kolor_tresc}><center>{tresc}</center></h2>\n</body></html>")
        Pelna_nazwa.close()
        ostatnie = input("\n----- POMYŚLNIE UKOŃCZONO TWORZENIE STRONY -----\n\n\n0. Wyjście\n1. Wróc do początku\n")
        if ostatnie == "1":
            return Menu().menu()
        elif ostatnie == "0":
            pass
        else:
            return Menu().menu()
        

o = Menu()
o.menu()











