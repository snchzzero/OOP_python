class Clock:
    def __init__(self, time=0):
        self.__time = time

    def set_time(self, tm=-1):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        #print(self.__time)
        return self.__time

    def __check_time(cls, tm):
        return True if type(tm) == int and 0 <= tm < 100000 else False



clock = Clock(4530)


clock.get_time()
assert isinstance(clock, Clock) and hasattr(Clock, 'set_time') and hasattr(Clock, 'get_time'), "в классе Clock присутствуют не все методы"

assert clock.get_time() == 4530, "текущее время в объекте clock не равно 4530"

clock.set_time(10)
assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
clock.set_time(-10)
assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
clock.set_time(1000001)
assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"