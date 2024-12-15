class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print(self.x + other.x, self.y + other.y)

    def distance(self, x, y):
        print(((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5)

    def symmertical_point(self):
        print(self.x, -self.y)

p1 = Point(3, 4)
p2 = Point(1, 2)
p1.distance(4, 5)
p2.symmertical_point()
p3 = p1 + p2