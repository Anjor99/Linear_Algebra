from src.linalg.vector import Vector
from src.linalg.matrix import Matrix

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
    
    def read_matrix(self, name):
        rows = int(input(f"\nEnter the number of rows for {name}: "))
        cols = int(input(f"\nEnter the number of cols for {name}: "))
        data = []
        
        for row in range(rows):
            new_row=[]
            for col in range(cols):
                val=float(input(f"Enter value for row {row + 1} and col {col + 1} of matrix {name}: "))
                new_row.append(val)
            data.append(new_row)
            
        return Matrix(data)