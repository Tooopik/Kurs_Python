'''

Mierzenie wydajnosci skryptu

'''
import time


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


start = time.perf_counter()
print('1 :', suma_1(100000000))
end = time.perf_counter()
print('T1 :', end - start)
print()

start = time.perf_counter()
print('2 :', suma_2(100000000))
end = time.perf_counter()
print('T2 :', end - start)
print()

start = time.perf_counter()
print('3 :', suma_3(100000000))
end = time.perf_counter()
print('T3 :', end - start)
print()

start = time.perf_counter()
print('4 :', suma_4(100000000))
end = time.perf_counter()
print('T4 :', end - start)
print()

start = time.perf_counter()
print('5 :', suma_5(100000000))
end = time.perf_counter()
print('T5 :', end - start)
