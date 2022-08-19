# Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/ZTCdEB_6h1I
# Подвиг 7. Объявите в программе следующие несколько классов:
# CPU - класс для описания процессоров;
# Memory - класс для описания памяти;
# MotherBoard - класс для описания материнских плат.
# Обеспечить возможность создания объектов каждого класса командами:
# cpu = CPU(наименование, тактовая частота)
# mem = Memory(наименование, размер памяти)
# mb = MotherBoard(наименование, процессор, память1, память2, ..., памятьN)
# Обратите внимание при создании объекта класса MotherBoard можно передавать несколько объектов класса Memory,
# максимум N - по числу слотов памяти на материнской плате (по умолчанию N = 4).
# Объекты классов должны иметь следующие локальные свойства:
# для класса CPU: name - наименование; fr - тактовая частота;
# для класса Memory: name - наименование; volume - объем памяти;
# для класса MotherBoard: name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число
# слотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - список из объектов класса Memory
# (максимум total_mem_slots штук по максимальному числу слотов памяти).
#
# Класс MotherBoard должен иметь метод get_config(self) для возвращения текущей конфигурации компонентов на материнской
# плате в виде следующего списка из четырех строк:
# ['Материнская плата: <наименование>',
# 'Центральный процессор: <наименование>, <тактовая частота>',
# 'Слотов памяти: <общее число слотов памяти>',
# 'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']
# Создайте объект mb класса MotherBoard с одним CPU (объект класса CPU) и двумя слотами памяти (объекты класса Memory).
# P.S. Отображать на экране ничего не нужно, только создать объект по указанным требованиям.
class CPU():
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr
class Memory():
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
class MotherBoard():
    def __init__(self, name, cpu, mem_slots, total_mem_slots=4):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
        self.mem_slots = mem_slots[:total_mem_slots]  # чтобы не более 4ех
    def get_config(self):
        s = str('Память: ')
        for i in self.mem_slots:
            s += f'{i.name} - {i.volume}; '
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}', s[:-2]
                ]
cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone2', 5000)
#mem1, mem2, mem3, mem4 = Memory('Kingstone', 4000), Memory('Kingstone2', 5000), Memory('Kingstone3', 6000), Memory('Kingstone4', 7000)
mb = MotherBoard('Asus', cpu, [mem1, mem2])
print(mb.get_config())


