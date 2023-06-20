from abc import ABC, abstractmethod


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        pass


class Stack(StackInterface):
    def __init__(self, top=None):
        self._top = top

    def push_back(self, obj):
        if self._top is None:
            self._top = obj
        else:
            obj_iter = self._top
            while obj_iter._next is not None:
                obj_iter = obj_iter._next
            obj_iter._next = obj

    def pop_back(self):
        obj_iter = self._top
        obj_prev = None
        if obj_iter:
            while obj_iter._next is not None:
                obj_prev = obj_iter
                obj_iter = obj_iter._next
            if obj_prev:
                obj_prev._next = None
            else:
                self._top = None
        return obj_iter


class StackObj:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next


# st = Stack()
# del_obj = st.pop_back()
#
# st.push_back(StackObj("obj 1"))
# obj = StackObj("obj 2")
# st.push_back(obj)
# st.push_back(StackObj("obj 3"))
# st.push_back(StackObj("obj 44"))
# st.push_back(StackObj("obj 55"))
# del_obj = st.pop_back()
# st.push_back(StackObj("obj 6"))
# # del_obj - ссылка на удаленный объект (если объектов не было, то del_obj = None)

assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

try:
    a = StackInterface()
    a.pop_back()
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"


st = Stack()
assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

obj_top = StackObj("obj")
st.push_back(obj_top)

assert st._top == obj_top, "неверное значение атрибута _top"

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top
while h:
    assert h._data == "obj", "неверные данные в объектах стека"
    h = h._next
    n += 1

assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"





