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
    
    def push_front(self, obj):
        if self.top is None:
            self.top = obj
        else:
            start_old = self.top
            self.top = obj
            start_new = obj
            while start_old.next != None:
                start_new.next = start_old
                start_old = start_old.next
                start_new = start_new.next
            start_new.next = start_old

    def validate(self, key):
        if self.top != None:
            total = 0
            start = self.top
            while start.next != None:
                start = start.next
                total += 1
            total += 1
            if 0 <= key < total:
                return True
            else:
                return False
        else:
            return False

    def __getitem__(self, key):
        if self.validate(key):
            total = 0
            start = self.top
            while start.next != None and total < key:
                start = start.next
                total += 1
            return start.data
        else:
            raise IndexError('неверный индекс')

    def __setitem__(self, key, value):
        if self.validate(key):

            start = self.top
            prev = start
            total = 0
            while start.next != None:
                if total == key and isinstance(value, StackObj):
                    if key == 0:
                        self.top = value
                    start = prev.next.next
                    prev.next = value
                    value.next = start
                    total += 1
                    continue
                elif total == key and (isinstance(value, StackObj) != True):
                    start.data = value
                    break
                prev = start
                start = start.next
                total += 1

        else:
            raise IndexError('неверный индекс')

    def __iter__(self):
        self.start = self.top
        return self
    
    def __next__(self):
        if self.start != None:
            while self.start.next != None or self.start != None:
                obj = self.start
                self.start = self.start.next
                return obj
            obj = self.start
            self.start = None
            return obj
        else:
            raise StopIteration
        
    

class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None
    


# st = Stack()
# st.push_back(StackObj("2"))
# st.push_back(StackObj("3"))
# st.push_back(StackObj("4"))
# st.push_front(StackObj("1"))
# st.push_back(StackObj("5"))
# st.push_front(StackObj("0"))
# st.push_front(StackObj("-1"))
# st.push_front(StackObj("-2"))

# print(st[2])
# st[2] = StackObj("00")
# print(st[2])
#
# print(st[0])
# st[0] = StackObj("-111")
# print(st[0])
#
# for obj in st:  # перебор объектов стека (с начала и до конца)
#     print(obj.data)  # отображение данных в консоль

st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"