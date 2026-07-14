class Circle:
    
    def __init__(self, r):
        self.radius = r
        
    
    def area(self):
        print( 3.14 * self.radius**2)    
    def perimeter(self):
        print (3.14 * 2 * self.radius)
    
    
obj = Circle(15)

obj.area()
obj.perimeter()
    
    