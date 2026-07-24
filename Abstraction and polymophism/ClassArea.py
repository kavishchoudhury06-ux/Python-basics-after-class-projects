
from abc import ABC, abstractmethod



class area(ABC):
    @abstractmethod
    def area(self):
        pass

class calculate(area):
    def area(self, l, b):
        self.l = l
        self.b = b
        self.a = self.l*self.b
        print (self.a) 
    
    
obj = calculate()

obj.area(5,10)

        