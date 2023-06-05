class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp    # температура
        self.press = press  # давление
        self.wet = wet      # влажность


class TemperatureView(Observer):
    def __init__(self, temperature=None):
        self.temperature = temperature

    def update(self, data):
        super().update(data)
        self.temperature = data.temp
        print(f"Текущая температура {self.temperature}")


class PressureView(Observer):
    def __init__(self, pressure=None):
        self.pressure = pressure

    def update(self, data):
        super().update(data)
        self.pressure = data.press
        print(f"Текущее давление {self.pressure}")


class WetView(Observer):
    def __init__(self, wet=None):
        self.wet = wet

    def update(self, data):
        super().update(data)
        self.wet = data.wet
        print(f"Текущая влажность {self.wet}")


subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

subject.change_data(Data(23, 150, 83))
# выведет строчки:
# Текущая температура 23
# Текущее давление 150
# Текущая влажность 83
subject.remove_observer(wet)
subject.change_data(Data(24, 148, 80))
# выведет строчки:
# Текущая температура 24
# Текущее давление 148