class Rectangle(object):

    def __init__(self, x1: int, x2: int, y1: int, y2: int):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    @property
    def is_square(self):
        return abs(self.x2 - self.x1) == abs(self.y2 - self.y1)


class Universe(object):

    def __init__(self, width: int, height: int, x_measurements: list, y_measurements: list):
        self.x_measurements = [0] + x_measurements + [width]
        self.y_measurements = [0] + y_measurements + [height]

    def rectangles(self):
        for x1 in self.x_measurements:
            for x2 in self.x_measurements:
                for y1 in self.y_measurements:
                    for y2 in self.y_measurements:
                        if x1 != x2 and y1 != y2:
                            yield Rectangle(x1, x2, y1, y2)
