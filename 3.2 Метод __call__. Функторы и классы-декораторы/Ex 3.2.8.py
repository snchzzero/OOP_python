class HandlerGET:
    def __init__(self, func):
        self.func = func

    def get(self, func, request, *args, **kwargs):
        if "method" in request.keys() and request["method"] == "GET" or "method" not in request.keys():
            return(f"GET: {self.func(request)}")
        elif "method" in request.keys() and request["method"] == "Post":
            return None
    def __call__(self, *args, **kwargs):
        return self.get(self.func, args[0])


# @HandlerGET
# def contact(request):
#     return "Сергей Балакирев"
#
# res = contact({"method": "GET", "url": "contact.html"})
# print(res)

@HandlerGET
def index(request):
    return "главная страница сайта"

res = index({"method": "GET"})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"