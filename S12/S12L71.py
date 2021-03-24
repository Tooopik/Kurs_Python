# 1
with open('oceany.txt', 'r', encoding='UTF_8') as file:
    oceany = file.read().splitlines()
    print('1:', oceany)

# 2
with open('oceany.txt', 'r', encoding='UTF_8') as file:
    oceany1 = file.readline()
    oceany2 = file.readline()
    oceany3 = file.readline()
    print('2:', oceany1)
    print('2:', oceany2)
    print('2:', oceany3)

# 3
with open('oceany.txt', 'r', encoding='UTF_8') as file:
    oceany4 = file.readlines()
    print('3:', oceany4)

# 4
with open('oceany.txt', 'r', encoding='UTF_8') as file:
    for line in file:
        print('4:', line)
