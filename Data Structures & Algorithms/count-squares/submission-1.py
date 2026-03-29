from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        print(point, self.points)
        squares = 0
        copy = self.points.copy()
        while copy:
            print(squares, copy)
            p, q = copy.popitem()
            print(p, q)
            # a 90 degree with the same size has the following property
            # abs(p0[x]-p1[x]) == abs(p1[y]-p2[y]) and abs(p0[y]-p1[y]) == abs(p1[x]-p2[x])
            # e,g, p0 = (1,1) and p1 = (2,2) => ((3,1) and (2,0)) or ((1,3) and (0,2))
            # bcs abs(2-1)=abs(1-y2)=>1=1-y2 or 1=y2-1=> y2=0 or y2=2
            # and abs(2-1)=abs(1-x2)=>1=1-x2 or 1=x2-1=> x2=0 or x2=2
            # where p2 is connected to p0
            # Now, given 3, the last one can gotten using the 3 points we have using the same property above
            # abs(p1[x]-p0[x]) == abs(p0[y]-p3[y]) and abs(p1[y]-p0[y]) == abs(p0[x]-p3[x])
            # and 
            # abs(p2[x]-p0[x]) == abs(p0[y]-p3[y]) and abs(p2[y]-p0[y]) == abs(p0[x]-p3[x])
            # cand1 = (x, y)
            #
            # point = (2,1), p = (1,2)
            dx = p[0]-point[0] # dx =  1
            dy = p[1]-point[1] # dy = -1
            x2 = point[0] + dy # x2 = 1 - 1 = 0
            y2 = point[1] - dx # y2 = 2 - 1 = 1
            print(p,(x2,y2))
            if (x2, y2) in copy:
                x3 = p[0] + dy # => x3 = 1 + 3 = 4
                y3 = p[1] - dx # => y3 = 2 - 2 =  0
                print(p,(x2,y2),(x3,y3))
                squares += q*self.points[(x2,y2)]*self.points[(x3,y3)]

            x2 = point[0] - dy
            y2 = point[1] + dx
            print(p,(x2,y2))
            if (x2, y2) in copy:
                x3 = p[0] - dy
                y3 = p[1] + dx
                print(p,(x2,y2),(x3,y3))
                squares += q*self.points[(x2,y2)]*self.points[(x3,y3)]
        return squares
