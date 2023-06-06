vector_log = []

def class_log(vector_l):
    def decorator(func):
        methods = {k: v for k, v in func.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(func, k, logger(v, k))
        return func
    def logger(func, k):
        def wrapper(self, *args, **kwargs):
            vector_l.append(k)
            return func(self, *args, **kwargs)

        return wrapper
    return decorator


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
print(v[0])