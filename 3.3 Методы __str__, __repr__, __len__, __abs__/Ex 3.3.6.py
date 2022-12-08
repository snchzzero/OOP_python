class LinkedList:
    def __init__(self, head=None, tail=None, l1=[]):
        self.head = head
        self.tail = tail
        self.l1 = l1

    def add_obj(self, obj):
        if self.head == None:
            self.head, self.tail = obj, obj
        else:
            self.tail.__next = obj
            obj.__prev = self.tail
            self.tail = obj
        self.l1.append(obj)
        #print(obj.__dict__)

    def remove_obj(self, indx):
        total = 0
        obj = self.head
        while total < indx:
            obj = obj.__next
            total += 1
        if obj != self.tail and obj != self.head:
            obj.__prev.__next = obj.__next
            obj.__next.__prev = obj.__prev
        elif obj == self.tail and len(self.l1) > 1:
            obj.__prev.__next = None
            self.tail = obj.__prev
            print(obj.__dict__)
            print(obj.__prev.__dict__)
            print(obj.__prev.__next.__dict__)
        elif obj == self.head and len(self.l1) > 1:
            obj.__next.__prev = None
            self.head = obj.__next
        if len(self.l1) > 0:
            # print(f'head: {self.head.__dict__}')
            # print(f'tail: {self.tail.__dict__}')
            # print(f'obj_del: {obj.__dict__}')
            self.l1.pop(indx)
        if len(self.l1) == 0:
            self.head, self.tail = None, None

    def __len__(self):
        return len(self.l1)

    def __call__(self, *args, **kwargs):
        #print(self.linked_lst(args[0]))
        #print(self.l1[args[0]].data)
        return self.linked_lst(args[0])

    def linked_lst(self, index):
        #print(self.l1[index].data)
        return self.l1[index].__data


class ObjList:
    def __init__(self, data, prev=None, next=None):
        self.__data = data
        self.__prev = prev
        self.__next = next

    def __getattr__(self, key):
        if key in ['_ObjList__data', '_LinkedList__data']:
            return self.__dict__["_ObjList__data"]
        elif key in ['_ObjList__next', '_LinkedList__next']:
            print(self.__dict__)
            return self.__dict__["_ObjList__next"]
        elif key in ['_ObjList__prev', '_LinkedList__prev']:
            return self.__dict__["_ObjList__prev"]

    def __setattr__(self, key, value):
        if key in ['_ObjList__data', '_LinkedList__data']:
            self.__dict__["_ObjList__data"] = value
        elif key in ['_ObjList__next', '_LinkedList__next']:
            self.__dict__["_ObjList__next"] = value
        elif key in ['_ObjList__prev', '_LinkedList__prev']:
            self.__dict__["_ObjList__prev"] = value

    # @property
    # def prev(self):
    #     return self.__prev
    #
    # @prev.setter
    # def prev(self, obj):
    #     self.__prev = obj
    #
    # @property
    # def next(self):
    #     return self.__next
    #
    # @next.setter
    # def next(self, obj):
    #     self.__next = obj
    #
    # @property
    # def data(self):
    #     return self.__data

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
#ln.add_obj(ObjList("Python ООП"))
#ln.add_obj(ObjList("Python ООП2"))
#ln.add_obj(ObjList("Python ООП3"))
ln.remove_obj(1)
#ln.remove_obj(0)
#ln.remove_obj(0)
#ln.remove_obj(0)
#ln.remove_obj(2)
#ln.remove_obj(1)
#ln.remove_obj(0)
#ln.remove_obj(0)
print(ln.head)
print(ln.tail)
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