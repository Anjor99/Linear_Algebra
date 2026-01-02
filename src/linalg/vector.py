class Vector:
    def __init__(self,components):
        self.components = components
    
    def add(self, other):
        if(len(self.components) != len(other.components)):
            raise ValueError("Vector Dimensions are not matching")
        result = Vector([])
        for a,b in zip(self.components, other.components):
            result.components.append(a + b)       
        return result
            
    def scalar_multiply(self,scalar):
        result = Vector([])
        for i in self.components:
            result.components.append(i*scalar)
        return result
    
    def magnitude(self):
        square_arr = sum([i**2 for i in self.components])
        return square_arr**0.5
    
    def unit_vector(self):
        magnitude = self.magnitude()
        return self.scalar_multiply(1/magnitude)