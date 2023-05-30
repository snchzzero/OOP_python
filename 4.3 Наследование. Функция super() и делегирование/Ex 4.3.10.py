class StringDigit(str):
    def __init__(self, string):
        if string.isdigit():
            super().__init__()
        else:
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        if self.isdigit() and other.isdigit():
            new_string = ''.join([self, other])
            return StringDigit(new_string)
        raise ValueError("в строке должны быть только цифры")

    def __radd__(self, other):
        if self.isdigit() and other.isdigit():
            new_string = ''.join([other, self])
            return StringDigit(new_string)
        raise ValueError("в строке должны быть только цифры")



#sd = StringDigit("12455752345950")
#sd2 = StringDigit("124557523459s50")
sd = StringDigit("123")
print(sd)       # 123
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
sd = sd + "12f" # ValueError