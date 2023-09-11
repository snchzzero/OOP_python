class Point:
    def __init__(self, x=0, y=0):
        # x, y = self.check(x, y)
        self._x = x
        self._y = y

    # def check(self, x, y):
    #     try:
    #         if all([ix in '.0123456789-' for ix in x]) and all([iy in '.0123456789-' for iy in y]):
    #             x = float(x) if '.' in x else int(x)
    #             y = float(y) if '.' in y else int(y)
    #         else:
    #             raise TypeError
    #     except Exception:
    #         x, y = 0, 0
    #     finally:
    #         print('Point: x = {}, y = {}'.format(x, y))
    #         return x, y


x, y = input().split()
try:
    if all([ix in '.0123456789-' for ix in x]) and all([iy in '.0123456789-' for iy in y]):
        x = float(x) if '.' in x else int(x)
        y = float(y) if '.' in y else int(y)
    else:
        raise TypeError
except Exception:
    x, y = 0, 0
finally:
    print('Point: x = {}, y = {}'.format(x, y))
    pr = Point(x, y)



# pt_1 = Point(x, y)
# x, y = input().split()
# pt_2 = Point(x, y)
# # x, y = input().split()
# # pt = Point(x, y)
