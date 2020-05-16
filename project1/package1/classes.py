import numpy as np

class A:
    def __init__(self, name : str):
        self.name = name

    def __str__(self):
        return f'{__class__}: name={self.name}'


class B:
    def __init__(self, name : str):
        self.name = name

    def __str__(self):
        return f'{__class__}: name={self.name}'


