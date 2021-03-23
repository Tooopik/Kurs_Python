from enum import IntEnum

MenuPogoda = IntEnum('Pogda', 'Słonce Deszcz Wiatr Chmury')

wybor = 2

if wybor == MenuPogoda.Deszcz:
    print(MenuPogoda.Deszcz)

else:
    print('NIC')
