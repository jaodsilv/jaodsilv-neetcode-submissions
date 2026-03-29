from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        verified = set()
        res = 0
        for p1 in self.points.keys():
            verified.add(p1)
            dx = p1[0]-point[0]
            dy = p1[1]-point[1]
            # Find squares made of this point `p` and point `point`
            # We must find the points that is opposed to p and the points that is opposed to q
            p2 = (point[0]+dy, point[1]-dx)
            if p2 in self.points and p2 not in verified:
                p3 = (p1[0]+dy, p1[1]-dx)
                if p3 in self.points:
                    res += self.points[p1]*self.points[p2]*self.points[p3]

            p2 = (point[0]-dy, point[1]+dx)
            if p2 in self.points and p2 not in verified:
                p3 = (p1[0]-dy, p1[1]+dx)
                if p3 in self.points:
                    res += self.points[p1]*self.points[p2]*self.points[p3]

        return res
