'''
다음 코드가 동작하도록 차 클래스를 정의하라.

>> car1 = car(2, 1000)
>> car1.wheel
2
>> car1.price
1000
'''


class car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price
