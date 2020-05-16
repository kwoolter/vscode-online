import numpy as np

class A:

    VECTOR_NORTH = np.array([0,1,0])
    VECTOR_SOUTH = np.array([0,-1,0])
    VECTOR_WEST = np.array([-1,0,0])
    VECTOR_EAST = np.array([1,0,0])
    VECTOR_UP = np.array([0,0,1])
    VECTOR_DOWN = np.array([0,0,-1])
    VECTOR_DUMMY = np.array([0,0,0])

    VALID_VECTORS = (VECTOR_NORTH, VECTOR_SOUTH, \
                    VECTOR_WEST, VECTOR_EAST, \
                    VECTOR_UP, VECTOR_DOWN, \
                    VECTOR_DUMMY)

    def __init__(self, name : str):
        self.name = name
        self.pos = np.array([0,0,0])
        self._old_pos = self.pos.copy()
        self.vector = A.VECTOR_DUMMY


    def __str__(self):
        return f'{__class__}: name={self.name} at {self.pos}'

    def move(self, direction : np.array = None, count : int = 1):
        self._old_pos = self.pos.copy()

        if direction is None:
            direction = self.vector

        self.pos = np.add(self.pos, direction * count)

        print(f'{self.name} moved from {self._old_pos} to {self.pos}')


class B:
    def __init__(self, name : str):
        self.name = name

    def __str__(self):
        return f'{__class__}: name={self.name}'


