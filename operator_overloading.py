class Complex:
    
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,other):
        return Complex(self.real+other.real,self.img+other.img)
    
    def __str__(self):
        return f"{self.img}i+ {self.real} j"

c1=Complex(4,5)
c2= Complex(3,4)
print(c1+c2)
    