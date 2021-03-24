'''

Podstawowe sposoby otwierania plików
r - Read (czytanie) - domyślne
w - Write (pisanie - jesli plik istniał to go usuniue, jeśli nie to stworzy
a - Append (dopisywanie) 

rozszerzenie to tylko 'teskst' nadawany po to aby inne programy rozpoznawały plik w odpowiedni dla tych programów sposób

'''
try:
    file = open('test2.txt', 'w')  # UCHWYT HANDLE
    file.write('sample')
    print(0/0)
    file.write('sample2')

finally:
    file.close()
