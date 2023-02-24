from abc import ABC,abstractmethod
#Abstract base classes
class GraphicShape(ABC):
    
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def calcArea(self):
        pass
class Circle(GraphicShape):
    def  __init__(self,radius):
        self.radius = radius
    def calcArea(self):
        return 3.14 *(self.radius **2)

class Square(GraphicShape):
    def __init__(self, squareside):
        self.squareside = squareside
    def calcArea(self):
        return self.squareside **2
# An abstract class (a class with no solid method) cannot be instantiated by itself, so comment out
# g = GraphicShape()
c = Circle(3)
print(c.calcArea())
s= Square(2)
print(s.calcArea())