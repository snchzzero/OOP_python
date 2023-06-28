class Money:
    def __init__(self, value):
        self._money = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value

    def __setattr__(self, key, value):
        if key in ['_money', 'money'] and isinstance(value, (int, float)):
            self.__dict__['_money'] = value
        else:
            raise TypeError('сумма должна быть числом')


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)




class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"

# m1 = Money(12)
# m1.money = 50
# print(m1.money)

m1 = MoneyR(1)
m1_1 = MoneyR(11)
m2 = MoneyD(2)
m = m1 + 10
print(m)  # MoneyR: 11
m = m1 - 5.4
m = m1 + m1_1
m = m1 + m2  # TypeError