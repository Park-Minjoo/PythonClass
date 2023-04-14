'''
다음 코드가 동작하도록 Car 클래스를 정의하라. 단 Bicycle 클래스는 Car 클래스를 상속받는다.

>> bicycle = Car(2, 100)
>> bicycle.price
100
'''


class Bicycle(Car):
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price


class Bicycle(Car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)
