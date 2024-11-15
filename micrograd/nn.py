import random

from typing import List

from micrograd.engine import Value


class Module:

    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0.0
    

    def parameters(self):
        return []


class Neuron(Module):

    def __init__(self, nin, nonlin=True, activation="relu"):
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        self.b = Value(0)
        self.nonlin = nonlin
        self.activation = activation
    

    def __call__(self, x):
        activation = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        out = activation
        if self.nonlin:
            if activation == "relu":
                out = activation.relu()
            elif activation == "tanh":
                out = activation.tanh()
        return out
    

    def parameters(self):
        return self.w + [self.b]


    def __repr__(self):
        return f"Neuron({len(self.w)}, {self.activation})"


class Layer(Module):

    def __init__(self, nin, nout, **kwargs):
        self.neurons = [Neuron(nin, **kwargs) for _ in range(nout)]
    

    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        return outs[0] if len(outs) == 1 else outs
    

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]


    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"


class MLP(Module):

    def __init__(self, nin, nouts: List):
        sizes = [nin] + nouts
        self.layers = [Layer(sizes[i], sizes[i + 1], nonlin=i != len(nouts) - 1) for i in range(len(nouts))]


    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x


    def parameters(self):
        return [p for l in self.layers for p in l.parameters()]
    

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"
