'''
tell - mówi, gdzie skończyliśmy ostatnią operacje na pliku
seek - szuka (zmienia) - na miejsce wskazane przez nie

'''

with open('oceany.txt', 'r', encoding='UTF-8') as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())
    print(file.tell())
    file.seek(4)
    print(file.tell())
    print(file.readline())
    print(file.tell())
