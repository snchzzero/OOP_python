class FileAcceptor:
    def __init__(self, *args):
        if type(args[0]) != list:
            self.list = list(args)
        else:
            self.list = list(set((args[0])))

    def __call__(self, *args, **kwargs):
        #print(args[0].split(".")[-1])
        return args[0].split(".")[-1] in self.list

    def __add__(self, other):
        return FileAcceptor(self.list + other.list)


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
filenames = list(filter(acceptor1 + acceptor2, filenames))
print(filenames)
