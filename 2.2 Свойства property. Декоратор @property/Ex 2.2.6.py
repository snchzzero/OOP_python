class StackObj:
    def __init__(self, data=None, next=None):
        self.__data = data
        self.__next = next
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next):
        if self.__check(next):
            self.__next = next

    def __check(self, next):
        if next.__class__ == StackObj:  # проверка, что __next будет ссылаться на объект класса StackObj
            return True

class Stack:
    def __init__(self):
        self.top = None
        self.data = []

    def push(self, obj):
        if len(self.data) == 0:
            self.data.append(obj)
            self.top = obj
        else:
            self.data[-1].next = obj
            self.data.append(obj)

    def pop(self):
        del_last_data = self.data.pop(-1)
        if len(self.data) == 0:
            self.top = None
        return del_last_data

    def get_data(self):
        l1 = list()
        for i in self.data:
            l1.append(i.data)
        return l1


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s2 = Stack()
top = StackObj("name_1")
s2.push(top)
obj = s2.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"
