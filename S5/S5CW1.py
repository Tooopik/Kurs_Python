findNumber = 40
guessNumber = 0

while guessNumber != findNumber:
    guessNumber = int(input('Guess a number : '))

    if findNumber == guessNumber:
        print('You guess ! That number is :', guessNumber)

    elif findNumber > guessNumber:
        print('Find number is greater than', guessNumber)

    else:
        print('Find number is smaller than', guessNumber)
