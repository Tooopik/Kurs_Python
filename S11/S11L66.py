import random
from enum import Enum


def drawn_event(eventList, eventProbability):
    drawnEvent = random.choices(eventList, eventProbability)[0]
    return drawnEvent


def drawn_colour(chestColourList, chestColoursProbability):
    drawnColour = random.choices(chestColourList, chestColoursProbability)[0]
    return drawnColour


def find_approximate_value(value, percentRange):
    lowestValue = value - ((percentRange / 100) * value)
    highestValue = value + ((percentRange / 100) * value)
    return random.randint(lowestValue, highestValue)


Event = Enum('Event', ['Chest', 'Empty'])
eventDictionary = {
    Event.Chest: 0.6,
    Event.Empty: 0.4
}
eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())

colours = Enum('Colours', {'Green': 'zielony',
                           'Orange': 'pomarańczowy',
                           'Purple': 'fioletowy',
                           'Gold': 'złoty'})

chestColoursDictionary = {colours.Green: 0.75,
                          colours.Orange: 0.2,
                          colours.Purple: 0.04,
                          colours.Gold: 0.01}

chestColourList = tuple(chestColoursDictionary.keys())
chestColoursProbability = tuple(chestColoursDictionary.values())

rewardForChest = {chestColourList[reward]: (
    reward + 1) * (reward + 1) * 1000 for reward in range(len(chestColourList))}

gameLenght = 5
goldAcquired = 0

print('Welcome in my game called GAME')

while gameLenght > 0:
    gamerAnswer = input('Do you want to move forward ? : ')

    if gamerAnswer == 'yes':
        print('Great, let\'s see what you got.... ')
        gameLenght -= 1
        drawnEvent = drawn_event(eventList, eventProbability)

        if drawnEvent == Event.Chest:
            print('You\'ve drawn a CHEST')
            drawnColour = drawn_colour(
                chestColourList, chestColoursProbability)

            if drawnColour == colours.Green:
                gamerReward = find_approximate_value(
                    rewardForChest[drawnColour], 10)
                goldAcquired = goldAcquired + gamerReward
                print('You\'ve drawn green chest ! :', gamerReward, 'gold')

            elif drawnColour == colours.Orange:
                gamerReward = find_approximate_value(
                    rewardForChest[drawnColour], 10)
                goldAcquired = goldAcquired + gamerReward
                print('You\'ve drawn orange chest !', gamerReward, 'gold')

            elif drawnColour == colours.Purple:
                gamerReward = find_approximate_value(
                    rewardForChest[drawnColour], 10)
                goldAcquired = goldAcquired + gamerReward
                print('You\'ve drawn purple chest !', gamerReward, 'gold')

            elif drawnColour == colours.Gold:
                gamerReward = find_approximate_value(
                    rewardForChest[drawnColour], 10)
                goldAcquired = goldAcquired + gamerReward
                print('You\'ve drawn gold chest !', gamerReward, 'gold')

        elif drawnEvent == Event.Empty:
            print('You\'ve drawn nothing, you are so unlucky!')

    else:
        print('You can move only forward man, nothing else')

print('Congratulation! You\'ve acquired', goldAcquired, 'gold')
