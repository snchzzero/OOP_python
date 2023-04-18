class Layer:
    def __init__(self, next_layer=None):
        self.name = 'Layer'
        self.next_layer = next_layer

class Input:  # формирование входного слоя нейронной сети
    def __init__(self, inputs):
        self.name = 'Input'
        self.inputs = inputs

class Dense:  # формирование полносвязного слоя нейронной сети
    def __init__(self, inputs, outputs, activation):
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
