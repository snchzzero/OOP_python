class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, name, value):
        if name == '_model' and isinstance(value, str):
            self.__dict__[name] = value
        elif name in ['_mass', '_speed', '_top'] and isinstance(value, (int, float)) and value > 0:
            self.__dict__[name] = value
        else:
            raise TypeError('неверный тип аргумента')


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, key, value):
        if key in ['_model', '_mass', '_speed', '_top']:
            super().__setattr__(key, value)
        elif key == '_chairs':
            if isinstance(value, int) and value > 0:
                self.__dict__[key] = value
            else:
                raise TypeError('неверный тип аргумента')


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, key, value):
        if key in ['_model', '_mass', '_speed', '_top']:
            super().__setattr__(key, value)
        elif key == '_weapons':
            if isinstance(value, dict) and all([isinstance(key, str) for key in value.keys()]) and \
                    all([isinstance(val, (int, float)) and val > 0 for val in value.values()]):
                self.__dict__[key] = value
            else:
                raise TypeError('неверный тип аргумента')


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
WarPlane(9, 7034, 34000, 2400, {"ракета": 2, "бомба": 7})
print(planes)