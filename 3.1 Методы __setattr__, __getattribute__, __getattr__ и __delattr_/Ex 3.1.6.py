class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        self.modules.pop(indx)

class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        self.lessons.pop(indx)

class LessonItem:
    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key == 'title' and type(value) == str:
            self.__dict__[key] = value
        elif (key == 'practices' or key == 'duration') and type(value) == int and value >= 0:
            self.__dict__[key] = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, item):  # при обращении к несуществующему атрибуту
        return False

    def __delattr__(self, item):
        if item == 'title' or item == 'practices' or item == 'duration':
            raise AttributeError(f"Атрибут {item} удалять запрещено.")

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)

l1 = LessonItem("Урок 5", 7, 1000)
print(l1.sad)
print(module_1.lessons)
module_1.remove_lesson(-1)
print(module_1.lessons)
print()
print(course.modules)
course.remove_module(-1)
print(course.modules)
del l1.title