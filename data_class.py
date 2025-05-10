from dataclasses import dataclass
@dataclass
class Number:
    name:str
    roll:int=0
    price:float=0.0
    
obj=Number("Python",12,123)
print(obj.name)
print(obj.roll)
print(obj.price)
    