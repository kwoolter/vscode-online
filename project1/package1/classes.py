import numpy as np

class A:
    def __init__(self, name : str):
        self.name = name
        self.pos = np.array([0,0,0])
        self.vector = np.array([1,0,0])


    def __str__(self):
        return f'{__class__}: name={self.name} at {self.pos}'

    def move(self, direction = None):
        if direction is None:
            direction = self.vector
        self.pos = np.add(self.pos, direction)


class B:
    def __init__(self, name : str):
        self.name = name

    def __str__(self):
        return f'{__class__}: name={self.name}'


