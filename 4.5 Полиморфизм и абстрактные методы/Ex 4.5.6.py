from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self):
        return 'Базовый класс Model'


class ModelForm(Model):
    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.__hash__()


    def __hash__(self):
        return hash((self._login, self._password))

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())
print(form.get_info())