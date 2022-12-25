class Circle():
    def __init__(self,r=0):
        self.r=r
    def area(self):
        t=3.14
        print(t*(self.r**2))

circle=Circle(4)
circle.area()