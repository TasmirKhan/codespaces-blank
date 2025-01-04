print("This is a practice file for OOPs in Python")
class circle:
   
    def __init__(self, radius=2):
        self.radius = radius
        print("New circle created with radius:",radius)

    def area(self):
        print("Area of the circle is ", 3.14*self.radius*self.radius)
        return 3.14*self.radius*self.radius

c1 = circle(4)
# c1.area()
print(c1.area())


