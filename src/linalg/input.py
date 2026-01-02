from src.linalg.vector import Vector

class Input:
    def __init__(self):
        pass

    def read_vector(self, name):
        size = int(input(f"Enter the size of vector {name}: "))
        values = []

        for i in range(size):
            val = float(input(f"Enter value {i + 1} for vector {name}: "))
            values.append(val)

        return Vector(values)