from abc import ABC, abstractmethod

class Absclass(ABC):
    def print(self, x):
       print("passed value", x) 
       
    @abstractmethod
    def task(self):
        pass
    
class test(Absclass):
    def task(self):
        print("inside test class")
        
obj = test()
obj.task()
obj.print(100)