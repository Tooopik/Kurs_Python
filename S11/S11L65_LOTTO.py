import random


def chose_random_numbers(amount=1, total_amount=1):
    if amount <= total_amount:
        numbers = []
        x = 0
        while x < amount:
            number = random.randint(1, total_amount)
            if number not in numbers:
                numbers.append(number)
                x = x + 1

        return numbers

    else:
        return False


def chose_random_numbers_2(amount=1, total_amount=1):
    if amount <= total_amount:
        return random.sample(range(1, total_amount + 1), amount)

    else:
        return False


print(chose_random_numbers_2(6, 49))
