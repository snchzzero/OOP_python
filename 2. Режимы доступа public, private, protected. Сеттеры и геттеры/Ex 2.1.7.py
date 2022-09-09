class Line:
    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_coords(self):
        return (self.__x1, self.__y1, self.__x2, self.__y2)


    def draw(self):
        print (self.__x1, self.__y1, self.__x2, self.__y2)

line = Line(1, 2, 3, 4)
print(line.get_coords())
line.draw()
line.set_coords(10, 20, 30, 40)
print(line.get_coords())
line.draw()
