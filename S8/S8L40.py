numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbersMultiply = {number: number * number for number in numbers}

print(numbersMultiply)

names = ['Adrian', 'Anna', 'Luksz', 'Kacper', 'Grzegorz']
namesLength = {name: len(name) for name in names}

print(namesLength)
