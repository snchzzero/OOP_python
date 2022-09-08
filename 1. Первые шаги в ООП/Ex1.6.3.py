#Подвиг 8. В программе объявлена переменная TYPE_OS и два следующих класса:
#TYPE_OS = 1 # 1 - Windows; 2 - Linux

#class DialogWindows:
#     name_class = "DialogWindows"
#
# class DialogLinux:
#     name_class = "DialogLinux"
# Необходимо объявить третий класс с именем Dialog, который бы создавал объекты командой:
# dlg = Dialog(<название>)
# Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
# Класс Dialog должен создавать объекты класса DialogWindows, если переменная TYPE_OS = 1 и
# объекты класса DialogLinux, если переменная TYPE_OS не равна 1. При этом, переменная TYPE_OS может меняться в
# последующих строчках программы. Имейте это в виду, при объявлении класса Dialog.
# P.S. В программе на экран ничего выводить не нужно. Только объявить класс Dialog.

TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"

class DialogLinux:
    name_class = "DialogLinux"

class Dialog:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            cls.__instance = super().__new__(DialogWindows)
            setattr(cls.__instance, 'name', *args)  #передаем новый аргумент name для нового экземпляра класса
            return cls.__instance
        elif TYPE_OS == 2:
            cls.__instance = super().__new__(DialogLinux)
            setattr(cls.__instance, 'name', *args)
            return cls.__instance

TYPE_OS = 1
d1 = Dialog("a")
print(d1)
print(d1.__dict__)

TYPE_OS = 2
d2 = Dialog("b")
print(d2)
print(d2.__dict__)

d3 = Dialog("c")
print(d3)
print(d3.__dict__)

TYPE_OS = 1
d4 = Dialog("e")
print(d4)
print(d4.__dict__)


# здесь объявляйте класс Dialog