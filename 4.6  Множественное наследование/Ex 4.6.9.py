class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if 'method' in request.keys() and request['method'] in self.allowed_methods:
            method_request = request.get('method').lower()
            return self.__getattribute__(method_request)(request)

        else:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")



class DetailView(RetriveMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
# print(html)   # GET: https://stepik.org/course/116336/

assert issubclass(DetailView, GeneralView), "класс DetailView должен наследоваться от класса GeneralView"


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST',)


view = DetailView()

try:
    html = view.render_request({'url': '123', 'method': 'POST'})
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError при вызове команды render_request({'url': '123', 'method': 'POST'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"

try:
    html = view.render_request({'url': '123', 'method': 'PUT'})
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при вызове команды render_request({'url': '123', 'method': 'PUT'}) при разрешенных методах allowed_methods = ('GET', 'POST', )"

html = view.render_request({'url': '123', 'method': 'GET'})
assert html == "GET: 123", "метод render_request вернул неверные данные"


class DetailView(RetriveMixin, UpdateMixin, CreateMixin, GeneralView):
    allowed_methods = ('GET', 'POST',)


view = DetailView()
html = view.render_request({'url': '123', 'method': 'POST'})
assert html == "POST: 123", "метод render_request вернул неверные данные"