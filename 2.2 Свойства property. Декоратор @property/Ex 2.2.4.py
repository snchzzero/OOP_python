
class Car:
    def __init__(self, model=None):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if self.__check(model):
            self.__model = model

    def __check(cls, model):
        if type(model) == str:
            if 2 <= len(model) <= 100:
                return True
    

car = Car()
car.model = 123
print(car.model)
car.model = 'd'
print(car.model)
car.model = "Toyota"
print(car.model)