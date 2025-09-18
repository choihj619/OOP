from abc import ABC,abstractmethod

class Shape3D:
    @abstractmethod
    def volume(self): pass

    @abstractmethod
    def surface_area(self): pass

    def describe(self):
        print(self.__class__.__name__)

class Cube(Shape3D):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def volume(self):
        return self.side ** 3
    
    def surface_area(self):
        return (self.side ** 2) * 6
    
class Sphere(Shape3D):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def volume(self):
        return (4 / 3) * 3.14 * self.radius ** 3
    
    def surface_area(self):
        return 4 * 3.14 * self.radius ** 2

class Cylinder(Shape3D):
    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius ** 2 * self.height
    
    def surface_area(self):
        return (2 * 3.14 * self.radius ** 2) + (self.height * 2 * 3.14 * self.radius) 

shapes = [Cube(2), Sphere(3), Cylinder(2,5)]
\
for s in shapes:
    s.describe()
    print("Volume:", s.volume())
    print("Surface area:", s.surface_area())
    print("---")
