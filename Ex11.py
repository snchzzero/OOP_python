# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/MAiCtExdo_k
# Подвиг 10. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
# add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже
# существует, то новое русское слово добавляется как синоним для перевода, например, go - идти, ходить, ехать);
# remove(self, eng) - для удаления связки по указанному английскому слову;
# translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов,
# соответствующих переводу английского слова, даже если в списке всего одно слово).
# Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
#
# tree - дерево
# car - машина
# car - автомобиль
# leaf - лист
# river - река
# go - идти
# go - ехать
# go - ходить
# milk - молоко
# Затем методом remove() удалите связку для английского слова car. С помощью метода translate()
# переведите слово go. Результат выведите на экран в виде строки из всех русских слов, связанных со словом go:
# Вывод в формате: идти ехать ходить

class Translator():
    slovar = {}
    def add(self, eng, rus):
        l1 = list()
        if eng in self.slovar:
            if type (self.slovar[eng]) == list:
                l1.extend(self.slovar[eng])
                l1.append(rus)
            else:
                l1.append(self.slovar[eng])
                l1.append(rus)
            self.slovar[eng] = l1
        else:
            self.slovar[eng] = rus

    def remove(self, eng):
        del self.slovar[eng]

    def translate(self, eng):
        if type(self.slovar[eng]) is not list:
            return [self.slovar[eng]]
        else:
            return (self.slovar[eng])

tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
print(*tr.translate('go'))
#print(tr.translate('tree')[0])

