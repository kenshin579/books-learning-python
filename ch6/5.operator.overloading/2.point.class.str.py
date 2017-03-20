class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

p1 = Point(2, 3)
p2 = Point(-1, 2)
print(p1)
print(p2)

print(p1 + p2)
