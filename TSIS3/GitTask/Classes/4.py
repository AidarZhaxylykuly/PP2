from math import sqrt
class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y        

    def dist(self, point):
        return sqrt((self.y - point.y)**2+(self.x - point.x)**2)
    
p1 = P(0, 0)
p2 = P(4, 4)
p1.show()
p2.show()
print(p1.dist(p2))
p1.move(1, 1)
p1.show()