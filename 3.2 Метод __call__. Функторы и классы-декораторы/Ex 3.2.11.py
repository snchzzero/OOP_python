class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):  # func - ссылка на декорируемую функцию
        def wrapper(*args, **kwargs):
            #print(func)
            #print(self.render)
            return [self.render(i) for i in func().split()]
        return wrapper

class RenderDigit:
    def __call__(self, *args, **kwargs):
        if args[0].isdigit() and args[0] not in (".") or (args[0].startswith('-') and args[0][1:].isdigit() and args[0][1:] not in (".")):
            return int(args[0])
        else:
            return None

@InputValues(RenderDigit())
def input_dg():
    return input()

res = input_dg()
print(res)

render = RenderDigit()
d1 = render("123")   # 123 (целое число)
d2 = render("45.54")   # None (не целое число)
d3 = render("-56")   # -56 (целое число)
d4 = render("12fg")  # None (не целое число)
d5 = render("abc")   # None (не целое число)

