from enum import IntEnum

Menu_Pogoda = IntEnum('Pogoda', 'Słońce Deszcz Wiatr Chmury')

wybor = int(input('Wybierz :'))

if wybor == Menu_Pogoda.Słońce:
    print('Słonce')
