from math import sqrt, pow


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        return float(sqrt(pow(x - self.x, 2) + pow(y - self.y, 2)))

