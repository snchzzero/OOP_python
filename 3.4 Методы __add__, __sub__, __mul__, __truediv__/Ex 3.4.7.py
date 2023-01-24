class Stack:
    def __init__(self):
        self.top = None

    def push_back(self, obj):
        if self.top is None:
            self.top = obj
        else:
            start = self.top
            while start.next != None:
                start = start.next
            start.next = obj

    def pop_back(self):
        start = self.top
        while start.next != None:
            prev = start
            start = start.next
        prev.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for obj in other:
            self.push_back(StackObj(obj))
        return self

    def __imul__(self, other):
        for obj in other:
            self.push_back(StackObj(obj))
        return self

class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None


    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value




# assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"
#
# st = Stack()
# top = StackObj("1")
# st.push_back(top)
# assert st.top == top, "неверное значение атрибута top"
# st.push_back(StackObj("2"))
# st = st + StackObj("3")
# st += StackObj("4")
# st = st * ['data_1', 'data_2']
# st *= ['data_55', 'data_66']
# st.pop_back()
# st += StackObj("100")
# st += StackObj("0")

# st.push_back(StackObj("3"))
# st.push_back(StackObj("4"))
# st.pop_back()
# st.push_back(StackObj("5"))
# st.push_back(StackObj("6"))
# st.pop_back()
# st.push_back(StackObj("7"))

assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"