class Shape:
    def __init__(self, x, y):        
        self.x = x                 
        self.y = y                 
    def move(self, delta_x, delta_y):  
        self.x = self.x + delta_x    
        self.y = self.y + delta_y


class Circle(Shape):
  pi = 3.14159
  all_circles = []
  def __init__(self,r=1,x=0,y=0):
    super().__init__(x,y)
    self.radius = r
    self.__class__.all_circles.append(self)

  @classmethod
  def total_area(cls):
    area = 0
    for circle in cls.all_circles:
      area += cls.circle_area(circle.radius)
    return area

  @staticmethod
  def circle_area(radius):
    return Circle.pi * radius * radius        
    

c1 = Circle(2,1,1)
c2 = Circle(4,3,2)
print(c1.radius, c1.x, c1.y)
print(c1.circle_area(c1.radius))
print(Circle.total_area())