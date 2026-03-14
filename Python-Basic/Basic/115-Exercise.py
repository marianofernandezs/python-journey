class Point:
    def __init__(self, x, y):
        self.x = x
        self. y = y
    def distance_calculate (self, other_point_x, other_point_y):
        distance_x = abs(self.x - other_point_x)
        distance_y = abs (self.y - other_point_y)
        return (distance_x ** 2 + distance_y ** 2) **0.5


mi_punto = Point(15, -15)

r = mi_punto.distance_calculate(1.3, 1.5)

print(r)
