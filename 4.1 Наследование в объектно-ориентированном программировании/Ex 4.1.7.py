class GenericView:
    def __init__(self, methods=('GET', 'POST')):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods):
        super().__init__()
        self.methods = methods

    def validate(self, method):
        return method in self.methods

    def get(self, request):
        if isinstance(request, dict):
            return f"url: {request['url']}"
        else:
            raise TypeError('request не содержит обязательного ключа url')

    def render_request(self, request, method):
        if self.validate(method):
            return getattr(self, method.lower())(request)
        else:
            raise TypeError('данный запрос не может быть выполнен')

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)






dv = DetailView(methods=('GET', 'POST'))
#dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')   # url: https://site.ru/home
html2 = dv.render_request({'url': 'https://site.ru/home'}, 'POST')   # url: https://site.ru/home
print(html)
print(html2)