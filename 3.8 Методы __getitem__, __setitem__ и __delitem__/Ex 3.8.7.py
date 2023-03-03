class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, obj):  # добавление объекта в конец списка
        if self.top is None:
            self.top = obj
        else:
            start = self.top
            while start.next != None:
                start = start.next
            start.next = obj

    def pop(self):  # удаление последнего объекта из списка
        start = self.top
        while start.next != None:
            previous = start
            start = start.next
        previous.next = None
        return start

    def __getitem__(self, item):
        if self.validate(item):
            total = 0
            start = self.top
            while total < item:
                start = start.next
                total += 1
            return start

    def __setitem__(self, item, value):
        if self.validate(item):
            total = 0
            start = self.top
            while total < item:
                previous = start
                start = start.next
                total += 1
            previous.next = value
            value.next = start.next

    def validate(self, item):
        len_c = 0
        start = self.top
        while start.next != None:
            start = start.next
            len_c += 1
        len_c += 1
        if 0 <= item < len_c and type(item) == int:
            return True
        else:
            raise IndexError('неверный индекс')







# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# print(st[2].data) # obj3
# print(st[1].data) # new obj2
# res = st[3] # исключение IndexError

st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"