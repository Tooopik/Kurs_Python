repeat = 0
total = 0

while repeat < 3:
    number = int(input('Give me a plus number : '))
    if number % 2 == 0 and number >= 0:
        total += number
        repeat += 1
        print('Actual add total : ', total)

    else:
        print('Try again')
        continue

print('Total :', total)
