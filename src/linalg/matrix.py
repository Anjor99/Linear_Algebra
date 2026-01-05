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
                
    def show(self):
        for row in self.data:
            print(" ".join(str(col) for col in row))

            
            