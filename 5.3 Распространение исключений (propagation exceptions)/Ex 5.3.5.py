class ValidatorString:
    def __init__(self, min_length, max_length, chars=None):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        try:
            if type(string) == str and self.min_length <= len(string) <= self.max_length:
                if not self.chars:
                    return string
                if any([s in self.chars for s in string]):
                    return string
            raise ValueError('недопустимая строка')
        except Exception:
            return None



class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request):
        if 'login' not in request or 'password' not in request:
            raise TypeError('в запросе отсутствует логин или пароль')
        for atr in ['_login', '_password']:
            if atr == '_login':
                value = self.login_validator.is_valid(request.get(atr[1:]))
            elif atr == '_password':
                value = self.password_validator.is_valid(request.get(atr[1:]))
            setattr(self, atr, value)
            # try:
            #     value = self.login_validator.is_valid(request.get(atr[1:]))
            #     setattr(self, atr, value)
            # except Exception:
            #     continue

        # self._login = self.login_validator.is_valid(request.get('login'))
        # self._passwor = self.password_validator.is_valid(request.get('password'))






login_v = ValidatorString(4, 50, )
password_v = ValidatorString(10, 50, "$#@%&?")
lg = LoginForm(login_v, password_v)
#login, password = input().split()
login, password = 'sergey', 'balakirev!'

try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)