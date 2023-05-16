class Layer:
    def __init__(self, next_layer=None):
        self.name = 'Layer'
        self.next_layer = next_layer

    def __call__(self, object):
        self.next_layer = object
        return object


class Input(Layer):  # формирование входного слоя нейронной сети
    def __init__(self, inputs):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):  # формирование полносвязного слоя нейронной сети
    def __init__(self, inputs, outputs, activation):
        super().__init__()
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:

    def __init__(self, layer):
        self.layer = layer
        self.next = self.layer

    def __iter__(self):
        return self

    def __next__(self):
        self.layer = self.next
        if self.layer != None:
            self.next = self.layer.next_layer
            return self.layer
        else:
            raise StopIteration










# first_layer = Layer()
# next_layer = first_layer(Layer())
# next_layer = next_layer(Layer())
# next_layer = next_layer(Layer())

nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu'))
layer = layer(Dense(layer.inputs, 2048, 'relu'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0
for x in NetworkIterator(nt):
    print(x)
    print(x.name)
    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"