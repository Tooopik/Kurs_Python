print("""
Witaj, w prostym kalkulatorze ;)""")
print("""wybierz porzadana operacje : 

+  - dodawanie
-  - odejmowanie
/  - dzielenie
*  - mnozenie
** - potegowanie
""")
operacja = input("wybrana operacja : ")

a = int(input("Podaj pierwsza liczbe : "))
b = int(input("Podaj druga liczbe : "))

if (operacja == '+'):
    print("Wynik dodawania", a, "do", b, "wynosi :", a + b)

elif (operacja == '-'):
    print("Wynik odejmowania", a, "od", b, "wynosi :", a - b)

elif (operacja == '/'):
    if (b == 0):
        print("Nie dziel przez zero !")
    else:
        print("Wynik dzielenia", a, "przez", b, "wynosi :", a / b)

elif (operacja == '*'):
    print("Wynik mnozenia", a, "przez", b, "wynosi :", a * b)

elif (operacja == '**'):
    print("Wynik potegowania", a, "do potegi", b, "wynosi :", a ** b)

else:
    print("Wybrano niepoprawna operacje!")
