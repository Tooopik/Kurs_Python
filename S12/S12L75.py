namesAndSurnames = []
with open('imionanazwiska.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        namesAndSurnames.append(tuple(line.replace('\n', '').split(" ")))


with open('imiona.txt', 'w', encoding='UTF-8') as file:
    for item in namesAndSurnames:
        file.write(item[0] + "\n")

with open('nazwiska.txt', 'w', encoding='UTF-8') as file:
    for item in namesAndSurnames:
        '''

        if (len(item)) == 2:
            file.write(item[1] + "\n")
        else:
            file.write('\n')

        '''
        try:
            file.write(item[1] + "\n")

        except IndexError:
            file.write('\n')
