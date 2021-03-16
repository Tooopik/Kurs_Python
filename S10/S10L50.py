
def suma_1(a):
    suma = 0
    for liczba in range(1, a + 1):
        suma = suma + liczba
    return suma


def suma_2(a):
    return (1 + a) / 2 * a


def suma_3(a):
    return sum([liczba for liczba in range(1, a + 1)])


def suma_4(a):
    return sum((liczba for liczba in range(1, a + 1)))


def suma_5(a):
    return sum({liczba for liczba in range(1, a + 1)})


print('1 :', suma_1(1000000))
print('2 :', suma_2(1000000))
print('3 :', suma_3(1000000))
print('4 :', suma_4(1000000))
print('5 :', suma_5(1000000))
