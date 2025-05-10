from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
        
    def area(self):
        return self.height*self.width
    
class Circle(Shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
    
    def area(self):
        return 3.14*self.height*self.height
    
class Triangle(Rectangle):
    def __inti__(self,heigth,width):
        super.__init__(heigth,width)
        
    def area(self):
        return (self.height*self.width)/2
    
r1= Rectangle(12,13)
print(r1.area())
c1= Circle(14,16)
print(c1.area())
t1= Triangle(12,13)
print(t1.area())

        