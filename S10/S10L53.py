'''
Domyslne argumenty
'''
import time

'''
def increment(x, amount=1):
    return x + amount


wartosc = int(input('Podaj wartosc : '))

print(increment(wartosc))

'''


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


def function_performace(func, arg, how_many_times=1):
    sum = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        stop = time.perf_counter()
        sum = sum + (stop - start)
    return sum


value = 12345
howManyTimes = 100

print(suma_1(value))
print(function_performace(suma_1, value, howManyTimes))
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
