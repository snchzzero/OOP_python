class WindowDlg:
    def __init__(self, title=None, width=None, height=None):
        self.__title = title
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if self.__check(width):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if self.__check(height):
            self.__height = height
            self.show()

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    def __check(cls, width_height):
        if type(width_height) == int:
            if 1 <= width_height <= 10000:
                return True

wnd = WindowDlg('Диалог 1', 100, 50)
wnd.show()
wnd.width = 300
wnd.height = 200

wnd.show
