class CountSquares:

    def __init__(self):
        self.points = defaultdict(int) # this stores point and count of it

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1,y1 = point
        count = 0
        for pt in self.points:
            x2,y2 = pt
            if abs(x1-x2) == abs(y1-y2) and x1 != x2 and y1 != y2:
                x3,y3 = x1,y2
                x4,y4 = x2,y1

                if (x3,y3) in self.points and (x4,y4) in self.points:
                    count += self.points[(x3,y3)] * self.points[(x4,y4)] * self.points[(x2,y2)]
        return count
