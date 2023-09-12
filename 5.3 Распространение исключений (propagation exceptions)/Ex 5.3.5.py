class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if not self.chars:
            if type(string) == str and self.min_length <= len(string) <= self.max_length:
                return True
            raise ValueError('недопустимая строка')
        elif type(string) == str and self.min_length <= len(string) <= self.max_length:
            lst = [s in self.chars for s in string]
            if any(lst):
                return True
            raise ValueError('недопустимая строка')
        raise ValueError('недопустимая строка')

class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request):
        if 'login' not in request and 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')
        if self.login_validator.is_valid(request.get('login')):
            if self.password_validator.is_valid(request.get('password')):
                self._login = request['login']
                self._password = request['password']



login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)