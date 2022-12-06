class LinkedList:
    def __init__(self, head=None, tail=None, l1=[]):
        self.head = head
        self.tail = tail
        self.l1 = l1

    def add_obj(self, obj):
        if self.head == None:
            self.head, self.tail = obj, obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj
        self.l1.append(obj)

    def remove_obj(self, indx):
        total = 0
        obj = self.head
        while total < indx:
            obj = obj.next
            total += 1
        if obj != self.tail and obj != self.head:
            obj.prev.next = obj.next
            obj.next.prev = obj.prev
        elif obj == self.tail and len(self.l1) > 1:
            obj.prev.next = None
            self.tail = obj.prev
        elif obj == self.head and len(self.l1) > 1:
            obj.next.prev = None
            self.head = obj.next
        elif len(self.l1) == 1:
            self.head = None
            self.tail = None
        self.l1.pop(indx)

    def __len__(self):
        return len(self.l1)

    def __call__(self, *args, **kwargs):
        #print(self.linked_lst(args[0]))
        #print(self.l1[args[0]].data)
        return self.linked_lst(args[0])

    def linked_lst(self, index):
        #print(self.l1[index].get_data())
        return self.l1[index].data


class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj

    @property
    def data(self):
        return self.__data

# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1) # s = Balakirev

ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
#ln.remove_obj(1)
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"