class LinkedList:
    head_t = 0
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj):
        print(f'В список добавлен элемент {obj}')
        if self.head_t == 0:
            self.head = obj
            self.tail = obj
            self.head_t = self.head_t + 1
            obj.set_prev = None
            #
            print(f'Перед объектом {obj} стоит объект {obj.get_prev()}')
            print(f'После объекта {obj} стоит объект {obj.get_next()}')
            print(f'Всего объектов в списке {self.head_t}')
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj
            self.head_t = self.head_t + 1
            print(f'Перед объектом {obj} стоит объект {obj.get_prev()}')
            print(f'После объекта {obj} стоит объект {obj.get_next()}')
            print(f'Всего объектов в списке {self.head_t}')

    def remove_obj(self):
        if self.head_t > 0:
            print(f'В списке удален последний элемент {self.tail}')
            self.tail.get_prev().set_next(None)
            self.tail = self.tail.get_prev()
            self.head_t = self.head_t - 1
            print(f'Теперь последний объект {self.tail}')
            print(f'Перед объектом {self.tail} стоит объект {self.tail.get_prev()}')
            print(f'После объекта {self.tail} стоит объект {self.tail.get_next()}')
            print(f'Всего объектов в списке {self.head_t}')



    def get_data(self):
        print(f'Возращение __data всех объектов списка {LinkedList.list}')
        print([i.get_data for i in LinkedList.list])

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

lst = LinkedList()
print(f'Создан объект LinkedList {lst}')
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
lst.remove_obj()

