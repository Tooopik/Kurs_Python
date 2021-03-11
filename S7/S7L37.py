definicje = {}

while True:
    print('Witaj w zbiorze ddefinicji, wybierz operacje : ')
    print('1 - wyszukaj definicje')
    print('2 - dodaj definicje')
    print('3 - usun definicje')
    print('4 - zakoncz')
    operacja = input(' Twój wybor : ')

    if operacja == '1':
        klucz = input('Podaj szukany klucz : ')
        if klucz in definicje:
            print(klucz, ':', definicje[klucz])

        else:
            print('Nieznam takiej definicji')

    elif operacja == '2':
        klucz = input('Podaj klucz : ')
        wartosc = input('Podaj wartosc : ')
        definicje[klucz] = wartosc
        print('Definicja dodana')

    elif operacja == '3':
        klucz = input('Poddaj klucz do usuniecia : ')
        if klucz in definicje:
            del definicje[klucz]
            print('Klucz zostal usuniety')

        else:
            print('Nie ma takiego klucza')

    elif operacja == '4':
        print('No to papapa')
        break

    else:
        print('BŁĄD, wybierz prawidłowa operacje')
