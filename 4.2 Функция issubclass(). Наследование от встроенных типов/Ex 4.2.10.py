class IteratorAttrs:
    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        if self.start < len(self.__dict__) - 1:
            for index, element in enumerate(self.__dict__.items()):
                if index == self.start:
                    self.start += 1
                    return element
        else:
            raise StopIteration


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory

phone = SmartPhone('nokia', (50, 120), 5)

for attr, value in phone:
    print(attr, value)