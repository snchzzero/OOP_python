class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_obj(self, obj, l1=[]):
        if self.head == None:
            self.head, self.tail = obj, obj
        else:
            self.tail.__next = obj
            obj.__prev = self.tail
            self.tail = obj
        self.l1.append(obj)

    def remove_obj(self, indx):
        total = 0
        obj = self.head
        while total < indx:
            obj = obj.__next
            total += 1
        if obj != self.tail and obj != self.head:
            obj.__prev.__next = obj.__next
            obj.__next.__prev = obj.__prev
        elif obj == self.tail:
            obj.__prev.__next = None
            self.tail = obj
        elif obj == self.head:
            obj.__next.__prev = None
            self.head = obj
        self.l1.remove(indx)

    def __len__(self):
        return len(self.l1)



class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next

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