import cmath


def pole_prosdtokata(a, b):
    return a * b


def pole_kwadratu(a):
    return a ** 2


def pole_trojkata(a, h):
    return a * h / 2


def pole_trapezu(a, b, h):
    return (a + b) * h / 2


def pole_kola(r):
    return cmath.pi * r ** 2


print('Witaj w kalkulatorze pol powerzchni figur')
while True:
    print('Jaka operacje chcesz wykonac ? : ')
    print('1 - pole prostokata')
    print('2 - pole kwadratu')
    print('3 - pole trojkata')
    print('4 - pole trapezu')
    print('5 - pole kola')
    print('6 - ZAKONCZ PROGRAM')

    wybor = input('Twoj wybor : ')

    if wybor == '6':
        print('BYE BYE')
        break

    elif wybor == '1':
        a = int(input('Podaj a : '))
        b = int(input('Podaj b : '))
        print('Pole prostokata wynosi :', pole_prosdtokata(a, b))

    elif wybor == '2':
        a = int(input('Podaj a : '))
        print('Pole kwaddratu wynosi :', pole_kwadratu(a))

    elif wybor == '3':
        a = int(input('Podaj a : '))
        h = int(input('Podaj h : '))
        print('Pole trojkata wynosi :', pole_trojkata(a, h))

    elif wybor == '4':
        a = int(input('Podaj a : '))
        b = int(input('Podaj b : '))
        h = int(input('Podaj h : '))
        print('Pole trapoezu wynosi :', pole_trapezu(a, b, h))

    elif wybor == '5':
        r = int(input('Podaj r : '))
        print('Pole koła wynosi :', pole_kola(r))

    else:
        print('BLAD, wybiez operacje z listy !')
