class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Let's skip the asteroid that will never meet anybody
        i = 0
        for ast in asteroids:
            if ast < 0:
                while i > 0 and asteroids[i-1] > 0 and asteroids[i-1] < -ast:
                    i -= 1
            if i == 0 or asteroids[i-1] < 0 or ast > 0:
                asteroids[i] = ast
                i += 1
            elif asteroids[i-1] == -ast:
                i -= 1
            else: # asteroids[i-1] > -ast
                pass
            # if i == 0:
                # print(i, j, asteroids[j-1])
            # else:
                # print(i, j, asteroids[i-1], asteroids[j-1], asteroids[:i])

        return asteroids[:i]
                    