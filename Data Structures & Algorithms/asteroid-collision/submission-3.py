class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Let's skip the asteroid that will never meet anybody
        i, j = 0, 0
        while j < len(asteroids):
            if i == 0 or asteroids[i-1] < 0 or asteroids[j] > 0:
                asteroids[i] = asteroids[j]
                i += 1
                j += 1
            else: # if asteroids[i-1] > 0 and asteroids[j] < 0
                if asteroids[i-1] == -asteroids[j]:
                    i -= 1
                    j += 1
                elif asteroids[i-1] < -asteroids[j]:
                    i -= 1
                else:
                    j += 1
            # if i == 0:
                # print(i, j, asteroids[j-1])
            # else:
                # print(i, j, asteroids[i-1], asteroids[j-1], asteroids[:i])

        return asteroids[:i]
                    