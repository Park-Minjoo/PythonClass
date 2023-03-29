# |Good parts:
# |- The code imports the `random` module to generate random numbers.
# |- The code uses a `for` loop to generate 6 random numbers between 1 and 45 and appends them to a list.
# |- The code returns the list of 6 random numbers.
# |
# |Bad parts:
# |- The code does not check if the generated numbers are unique. It is possible for the same number to be generated multiple times.
# |- The code does not sort the list of generated numbers in ascending order.
import random


def make_lotto():
    result = []
    for i in range(6):
        num = random.randint(1, 45)
        result.append(num)
    return result


print(make_lotto())
