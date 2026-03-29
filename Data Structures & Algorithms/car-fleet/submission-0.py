class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        # Let's first sort cars by position descending
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True) # O(n*log(n))
        print(cars)

        fleets = 1
        car = cars[0]
        for i in range(1, len(cars)):
            # If the next car speed is higher, it will eventually reach the current car.
            nextCar = cars[i]
            print(car, nextCar)
            if car[1] < nextCar[1]:
                # Then wee have to test if it will reach before or after target
                # p1+s1*t = p2+s2*t => p1-p2 = t(s2-s1) => t = (p1-p2)/(s2-s1)
                # p = p1+s1*(p1-p2)/(s2-s1)
                p = car[0] + car[1]*(car[0]-nextCar[0])/(nextCar[1]-car[1])
                if p > target:
                    fleets += 1
                    car = nextCar
                # else: We keep the same car to compute the fleet
            else:
                fleets += 1
                car = nextCar
        return fleets
