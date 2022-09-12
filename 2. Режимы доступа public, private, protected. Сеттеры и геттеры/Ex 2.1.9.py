class LinkedList:
    head_t = 0
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        #print(f'В список добавлен элемент {obj}')
        if self.head_t == 0:
            self.head = obj
            self.tail = obj
            self.head_t = self.head_t + 1
            obj.set_prev = None
            #
            #print(f'Перед объектом {obj} стоит объект {obj.get_prev()}')
            #print(f'После объекта {obj} стоит объект {obj.get_next()}')
            #print(f'Всего объектов в списке {self.head_t}')
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
            self.head_t = self.head_t + 1
            #print(f'Перед объектом {obj} стоит объект {obj.get_prev()}')
            #print(f'После объекта {obj} стоит объект {obj.get_next()}')
            #print(f'Всего объектов в списке {self.head_t}')

    def remove_obj(self):
        if self.head_t > 1:
            #print(f'В списке удален последний элемент {self.tail}')
            self.tail.get_prev().set_next(None)
            self.tail = self.tail.get_prev()
            self.head_t = self.head_t - 1
            #print(f'Теперь последний объект {self.tail}')
            #print(f'Перед объектом {self.tail} стоит объект {self.tail.get_prev()}')
            #print(f'После объекта {self.tail} стоит объект {self.tail.get_next()}')
            #print(f'Всего объектов в списке {self.head_t}')
        elif self.head_t == 1:
            #print(f'В списке удален последний элемент {self.tail}')
            self.tail = None
            self.head_t = None


    def get_data(self):
        #print(f'Возращение __data всех объектов списка')
        start = self.head
        l1 = list()
        #print(start.get_data())
        while start.get_next() != None and self.head != None and self.tail != None:
            l1.append(start.get_data())
            start = start.get_next()
        if start.get_next() == None and self.head != None and self.tail != None:
            l1.append(start.get_data())
        #print(l1)
        return l1


class ObjList:
    def __init__(self, data=None, next=None, prev=None):
        self.__next = next
        self.__prev = prev
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

# lst = LinkedList()
# print(f'Создан объект LinkedList {lst}')
# lst.add_obj(ObjList("данные 1"))
# lst.add_obj(ObjList("данные 2"))
# lst.add_obj(ObjList("данные 3"))
# lst.get_data()
# lst.remove_obj()
# lst.get_data()

ls = LinkedList()
ls.add_obj(ObjList("данные 1"))
ls.add_obj(ObjList("данные 2"))
ls.add_obj(ObjList("данные 3"))
ls.add_obj(ObjList("данные 34"))
assert ls.get_data() == ['данные 1', 'данные 2', 'данные 3', 'данные 34'], "метод get_data вернул неверные данные"

ls_one = LinkedList()
ls_one.add_obj(ObjList(1))
assert ls_one.get_data() == [1], "метод get_data вернул неверные данные"

h = ls_one.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 1, "неверное число объектов в списке: возможно некорректно работает метод add_obj"
ls_one.remove_obj()
assert ls_one.get_data() == [], "метод get_data вернул неверные данные для пустого списка, возможно, неверно работает метод remove_obj"

ls2 = LinkedList()
assert ls.head != ls2.head, "атрибут head должен принадлежать объекту класса LinkedList, а не самому классу"
assert ls.tail != ls2.tail, "атрибут tail должен принадлежать объекту класса LinkedList, а не самому классу"

h = ls.head
n = 0
while h:
    n += 1
    h = h.get_next()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.head
n = 0
while h:
    h = h._ObjList__next
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __next"

h = ls.tail
n = 0
while h:
    n += 1
    h = h.get_prev()

assert n == 4, "неверное число объектов в списке: возможно некорректно работает метод add_obj"

h = ls.tail
n = 0
while h:
    h = h._ObjList__prev
    n += 1

assert n == 4, "неверное число объектов в списке: возможно некорректные значения в атрибутах __prev"
