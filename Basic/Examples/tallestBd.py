def birthday_cake_candles(list):
    tallest = max(list)
    return list.count(tallest)


print(birthday_cake_candles([4, 4, 3, 2, 4]))
