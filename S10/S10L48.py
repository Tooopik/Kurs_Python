import Pola_figur
from enum import IntEnum

Menu_Figury = IntEnum(
    'Menu_Figury', 'Prostokat Kwadrat Trojkat Trapez Kolo Zakoncz')

print('Witaj w kalkulatorze pol powierzchni figur')
while True:
    print('''Jaka operacje chcesz wykonac ? :
    1 - pole prostokata
    2 - pole kwadratu
    3 - pole trojkata
    4 - pole trapezu
    5 - pole kola
    6 - ZAKONCZ PROGRAM''')

    wybor = int(input('Twoj wybor : '))

    if wybor == Menu_Figury.Zakoncz:
        print('BYE BYE')
        break

    elif wybor == Menu_Figury.Prostokat:
        a = int(input('Podaj a : '))
        b = int(input('Podaj b : '))
        print('Pole prostokata wynosi :', Pola_figur.pole_prostokata(a, b))

    elif wybor == Menu_Figury.Kwadrat:
        a = int(input('Podaj a : '))
        print('Pole kwadratu wynosi :', Pola_figur.pole_kwadratu(a))

    elif wybor == Menu_Figury.Trojkat:
        a = int(input('Podaj a : '))
        h = int(input('Podaj h : '))
        print('Pole trojkata wynosi :', Pola_figur.pole_trojkata(a, h))

    elif wybor == Menu_Figury.Trapez:
        a = int(input('Podaj a : '))
        b = int(input('Podaj b : '))
        h = int(input('Podaj h : '))
        print('Pole trapezu wynosi :', Pola_figur.pole_trapezu(a, b, h))

    elif wybor == Menu_Figury.Kolo:
        r = int(input('Podaj r : '))
        print('Pole kola wynosi :', Pola_figur.pole_kola(r))

    else:
        print('BLAD, wybierz operacje z listy !')
