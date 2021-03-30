def open_file(path):
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return file.read()

    except FileNotFoundError:
        print('Plik o  nazwie', path, 'nie istnieje')


nameOfFile = input("Podaj nazwę pliku do otwarcia :")
fileContent = open_file(nameOfFile)

print(fileContent)
