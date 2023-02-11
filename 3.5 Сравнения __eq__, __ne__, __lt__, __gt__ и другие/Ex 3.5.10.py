class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume

    def __eq__(self, other):
        if type(other) == int or type(other) == float:
            return (self.ro * self.volume) == other
        else:
            return (self.ro * self.volume) == (other.ro * other.volume)

    def __lt__(self, other):
        if type(other) == int or type(other) == float:
            return (self.ro * self.volume) < other
        else:
            return (self.ro * self.volume) < (other.ro * other.volume)

    def __le__(self, other):
        if type(other) == int or type(other) == float:
            return (self.ro * self.volume) <= other
        else:
            return (self.ro * self.volume) <= (other.ro * other.volume)

    def __gt__(self, other):
        if type(other) == int or type(other) == float:
            return (self.ro * self.volume) > other
        else:
            return (self.ro * self.volume) > (other.ro * other.volume)

    def __ge__(self, other):
        if type(other) == int or type(other) == float:
            return (self.ro * self.volume) >= other
        else:
            return (self.ro * self.volume) >= (other.ro * other.volume)
body1 = Body('body1', 6, 10)
body2 = Body('body1', 5, 10)
# print(body1 <= body2)  # True, если масса тела body1 больше массы тела body2
# print(body1 == body2) # True, если масса тела body1 равна массе тела body2
# print(body1 < 10)     # True, если масса тела body1 меньше 10
# print(body2 == 50)     # True, если масса тела body2 равна 5
print(50 == body1)