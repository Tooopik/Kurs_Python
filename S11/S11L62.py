from collections import Counter
import random


def will_weapon_hit(weaponChanceToHitPercentage):
    isHitChance = random.uniform(0, 100)
    if isHitChance < weaponChanceToHitPercentage:
        return True

    else:
        return False


listHit = []
x = 0
while x < 100:
    x = x + 1
    listHit.append(will_weapon_hit(50))

print(listHit.count(True))
print(listHit.count(False))

dictionaryHit = Counter(listHit)
print(dictionaryHit)
