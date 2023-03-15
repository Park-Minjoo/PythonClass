import random


def make_lotto():
    result = []
    for i in range(6):
        num = random.randint(1, 45)
        result.append(num)
    return result


print(make_lotto())
