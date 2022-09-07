class Server:
    total = 0
    ip = 0
    #buffer = []
    def __new__(cls, *args, **kwargs):
        cls.__instance = super().__new__(cls)
        cls.total += 1
        cls.__instance.ip = cls.total
        return cls.__instance

    def __init__(self):
        self.buffer = []

    def send_data(self, data):
        #Server.bufer.append(data)
        Router.buffer.append(data)
        #print(f'В буфер Роутера добавлен объект DATA {data}, сообщение {data.data}, ip {data.ip}')

    def get_data(self):
        if len(self.buffer) > 0:
            #print(Server.bufer)
            l1 = self.buffer.copy()
            self.buffer.clear()
            return l1
            #Server.bufer.clear()
            #print(Server.bufer)
        else:
            #print(Server.bufer)
            return self.buffer
    def get_ip(self):
        #print(self.ip)
        return self.ip

class Router:
    buffer = []
    link_server = []

    def link(self, server):
        print(f'Сервер: {server} ip {server.ip} подсоединен к роутеру')
        Router.link_server.append(server)
        print(f'Подключенные серверы: {Router.link_server}')
    def unlink(self, server):
        print(f'Сервер: {server} ip {server.ip} отсоединен от роутера')
        Router.link_server.remove(server)
        print(f'Подключенные серверы: {Router.link_server}')
    def send_data(self):
        print(f'Подключенные к роутеры сервера: {Router.link_server}')
        print(f'Пакеты Data для передачи с Роутера: {Router.buffer}')
        for buf in Router.buffer:
            for serv in Router.link_server:
                if serv.ip == buf.ip:
                    serv.buffer.append(buf)
                    print(f'Роутер отправил пакет DATA {buf}, Сообщение {buf.data}, на ip {buf.ip}')
                    print(f'В буфере Сервера {serv.ip} добавлен пакет {buf}, сообщение {buf.data}. Всего сообщение у Сервера {serv.ip}- {len(serv.buffer)}')
        Router.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip



assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())  # к роутеру подсоединилось 4 сервера
sv_to = Server()
router.link(sv_to)   # к роутеру подсоединяется 5ый сервер
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

print(f'Длинна буфера Сервера {sv_to.ip}- {len(msg_lst_to)}') # мой тест
assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"