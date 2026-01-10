import math

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
        if magnitude == 0:
            raise ValueError("Unit vector undefined due to 0 Magnitude")
        return self.scalar_multiply(1/magnitude)
    
    def dot(self,other):
        if (len(self.components)!=len(other.components)):
            raise ValueError("Dimensions are not matching")
        result=0
        for i in range(len(self.components)):
            result= self.components[i]*other.components[i]+result
        return result
    
    def angle_btn_vectors(self,other):
        denom = self.magnitude() * other.magnitude()
        if denom == 0:
            raise ValueError("Angle undefined for zero vector")
        cos_theta = self.dot(other) / denom
        cos_theta = max(-1, min(1, cos_theta))  # clamp
        return math.acos(cos_theta)
    
    def cos_similarity(self,other):
        denom = self.magnitude() * other.magnitude()
        if denom == 0:
            raise ValueError("Cosine similarity undefined for zero vector")
        return self.dot(other)/(self.magnitude()*other.magnitude())
    