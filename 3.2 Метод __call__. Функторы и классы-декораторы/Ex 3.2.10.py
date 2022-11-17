class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return [int(i) for i in self.func().split(" ")]

@InputDigits
def input_dg():
    vvod = input()
    return vvod

res = input_dg()
print(res)