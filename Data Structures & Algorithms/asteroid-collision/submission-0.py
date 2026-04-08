class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Let's skip the asteroid that will never meet anybody
        res = []
        i = 0
        while i < len(asteroids) and asteroids[i] < 0:
            res.append(asteroids[i])
            i += 1
        while i < len(asteroids):
            if len(res) == 0 or res[-1] < 0 or asteroids[i] > 0:
                res.append(asteroids[i])
                i += 1
            else: # if res[-1] > 0 and asteroids[i] < 0
                if res[-1] == -asteroids[i]:
                    res.pop()
                    i += 1
                elif res[-1] < -asteroids[i]: # and res[-1] > 0
                    res.pop()
                else:
                    i += 1
            

        return res
                    