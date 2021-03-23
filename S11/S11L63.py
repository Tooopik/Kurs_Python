import random
from collections import Counter

movieList = ['Tytyl 1', 'Tytul 2', 'Tytul 3', 'Tytul 4']
event = ['smierc', 'wygrana', 'przegrana', 'utrata zlota', 'utrata zycia']
nagrodaZeSkrzynki = ['Zielona', 'Pomaranczowa', 'Purpurowa', 'Legendarna']

print(random.choice(movieList))
print(Counter(random.choices(nagrodaZeSkrzynki, [80, 15, 3, 2], k=100)))
