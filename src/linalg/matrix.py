import math
from src.linalg.vector import Vector
class Matrix:
    def __init__(self, data ):
        self.data = data  # Initialize an empty list to hold matrix rows
        self.rows = len(self.data)
        self.cols = len(self.data[0]) if self.data else 0
        self.shape = (self.rows, self.cols)  # Initialize shape as (rows, cols)
        self._validate_shape()
    
    def _validate_shape(self):
        for row in self.data:
            if len(row) != self.cols:
                raise ValueError("Every row must have equal number of columns")
            
    def add(self,other):
        if self.shape != other.shape:
            raise ValueError("Both Matrices must have same shape for Matrix addition")
        
        result=[]
        
        for row_self,row_other in zip(self.data, other.data):
            new_row=[]
            for col_self,col_other in zip(row_self,row_other):
                new_row.append(col_self+col_other)
            result.append(new_row)
            
        return Matrix(result)
    
    def multiply(self,other):
        if (self.cols!=other.rows):
            raise ValueError("Cannot multiply given matrices , shared dimension not same")
        result = []
        rows = self.rows
        cols = other.cols
        shared_dim = self.cols
        for i in range(rows):
            new_row=[]
            for j in range(cols):
                total = 0
                for k in range(shared_dim):
                    total += self.data[i][k]*other.data[k][j]
                new_row.append(total)
            result.append(new_row)
        return Matrix(result)
    
    def transpose(self):
        result=[]
        tr_rows=self.cols
        tr_cols=self.rows
        for i in range(tr_rows):
            new_row=[]
            for j in range(tr_cols):
                new_row.append(self.data[j][i])
            result.append(new_row)
        return Matrix(result)
                
    def show(self):
        for row in self.data:
            print(" ".join(str(col) for col in row))
            
    def generate_identity(size):
        identity=[]
        for i in range(size):
            new_row=[]
            for j in range(size):
                if i==j:
                    new_row.append(1)
                else:
                    new_row.append(0)
            identity.append(new_row)
        return Matrix(identity)

            
    def inverse(self):
        if self.rows != self.cols:
            raise ValueError("Only square matrices can be inverted")
        
        n = self.rows
        identity = Matrix.generate_identity(n)
        augmented = [self.data[i] + identity.data[i] for i in range(n)]
        
        for i in range(n):
            pivot = augmented[i][i]
            if pivot == 0:
                raise ValueError("Matrix is singular and cannot be inverted")
            for j in range(2*n):
                augmented[i][j] /= pivot
            
            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2*n):
                        augmented[k][j] -= factor * augmented[i][j]
        
        inverse_data = [row[n:] for row in augmented]
        return Matrix(inverse_data)
    
    def det(self):
        if self.rows != self.cols:
            raise ValueError("Only square matrices have determinants")
        return self._det_recursive(self.data)

    def _det_recursive(self, matrix):
        n = len(matrix)

        # Base case: 1×1
        if n == 1:
            return matrix[0][0]

        # Base case: 2×2
        if n == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

        determinant = 0

        # Cofactor expansion along first row
        for col in range(n):
            sign = (-1) ** col
            submatrix = self._get_submatrix(matrix, 0, col)
            determinant += sign * matrix[0][col] * self._det_recursive(submatrix)

        return determinant

    def _get_submatrix(self, matrix, remove_row, remove_col):
        return [
            [matrix[i][j] for j in range(len(matrix)) if j != remove_col]
            for i in range(len(matrix)) if i != remove_row
        ]
        
    def multiply_vector(self, vector):
        if self.cols != len(vector.components):
            raise ValueError("Matrix columns must match vector size")

        result = []
        for row in self.data:
            total = 0
            for a, b in zip(row, vector.components):
                total += a * b
            result.append(total)

        return Vector(result)
    
    def is_eigenvector(self, vector, lam, tol=1e-6):
        Ax = self.multiply_vector(vector)
        lam_x = vector.scalar_multiply(lam)

        for a, b in zip(Ax.components, lam_x.components):
            if abs(a - b) > tol:
                return False
        return True

    
    def eigenvalues_2x2(self):
        if self.rows != 2 or self.cols != 2:
            raise ValueError("Eigenvalue solver only implemented for 2x2 matrices")

        a, b = self.data[0]
        c, d = self.data[1]

        trace = a + d
        determinant = a*d - b*c

        disc = trace**2 - 4 * determinant

        if disc < 0:
            return None  # no real eigenvalues

        sqrt_disc = math.sqrt(disc)

        lam1 = (trace + sqrt_disc) / 2
        lam2 = (trace - sqrt_disc) / 2

        return lam1, lam2

    def eigenvector_2x2(self, eigenvalue):
        if self.rows != 2 or self.cols != 2:
            raise ValueError("Eigenvector solver only implemented for 2x2 matrices")

        a, b = self.data[0]
        c, d = self.data[1]

        A = [[a - eigenvalue, b],
             [c, d - eigenvalue]]

        if A[0][0] != 0:
            x2 = 1
            x1 = -A[0][1] / A[0][0]
        elif A[1][0] != 0:
            x2 = 1
            x1 = -A[1][1] / A[1][0]
        else:
            x1, x2 = 1, 0

        return Vector([x1, x2])
