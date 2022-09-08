class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

class AppStore:
    app_list = list()

    def add_application(self, app):
        self.app = AppStore.app_list.append(app)
        print(AppStore.app_list)
    def remove_application(self, app):
        if app in AppStore.app_list:
            self.app = AppStore.app_list.remove(app)
            print(AppStore.app_list)
    def block_application(self, app):
        self.app = app.blocked = True
    def total_apps(self):
        return len(AppStore.app_list)

# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
#
# app_gmail = Application("Gmail")
# store.add_application(app_gmail)
# store.block_application(app_gmail)
#
# #store.remove_application(app_youtube)
# store.block_application(app_youtube)
# print(store.total_apps())

store = AppStore()
app_youtube = Application("Youtube")
assert app_youtube.blocked == False, "начальное значение blocked должно быть равно False"

store.add_application(app_youtube)
store.block_application(app_youtube)

assert app_youtube.name == "Youtube" and app_youtube.blocked == True, "неверные значения локальных атрибутов объекта класса Application"

app_stepik = Application("Stepik")
store.add_application(app_stepik)

assert store.total_apps() == 2, "неверное число приложений в магазине"

store.remove_application(app_youtube)
assert store.total_apps() == 1, "неверное число приложений в магазине, некорректно работает метод remove_application"