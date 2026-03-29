class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        memo = {}
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda x: x[0], reverse = True)
        fleets = 1
        prevTime = (target-cars[0][0]) / cars[0][1]
        for p, s in cars:
            time = (target-p) / s
            if time > prevTime:
                fleets += 1
                prevTime = time

        return fleets