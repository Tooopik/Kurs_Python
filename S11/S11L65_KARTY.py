import random


def deal_cards(cList, cardAmout):
    random.shuffle(cList)
    player1 = []
    player2 = []
    player3 = []
    player4 = []
    while len(player4) < cardAmout:
        player1.append(cList.pop())
        player2.append(cList.pop())
        player3.append(cList.pop())
        player4.append(cList.pop())

    return player1, player2, player3, player4


cardList = ['9', '9', '9', '9',
            '10', '10', '10', '10',
            'Jack', 'Jack', 'Jack', 'Jack',
            'Queen', 'Queen', 'Queen', 'Queen',
            'King', 'King', 'King', 'King',
            'Ace', 'Ace', 'Ace', 'Ace',
            'Joker', 'Joker']

print(deal_cards(cardList, 5))
