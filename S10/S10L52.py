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


def function_performace(func, arg):
    start = time.perf_counter()
    func(arg)
    stop = time.perf_counter()
    return stop - start


value = 123456789

print(suma_1(value))
print(function_performace(suma_1, value))
print()

print(suma_2(value))
print(function_performace(suma_2, value))
print()

print(suma_3(value))
print(function_performace(suma_3, value))
print()

print(suma_4(value))
print(function_performace(suma_4, value))
print()

print(suma_5(value))
print(function_performace(suma_5, value))
print()
