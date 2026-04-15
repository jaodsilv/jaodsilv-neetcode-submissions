class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        # L is the first asteroid to the right
        # R-1 is the last asteroid to the right
        # i is the index being processed
        # All between L-1 and R-1 are to the right
        L, R, i = 0, 0, 0
        for i, s in enumerate(asteroids):
            if s > 0:
                asteroids[R] = s
                if L is None:
                    L = R
                R += 1
            else:
                while R > L and asteroids[R-1] < -asteroids[i]:
                    R -= 1
                if L == R:
                    # -s is bigger than any asteroid alive to the left that are going to the right
                    asteroids[R] = asteroids[i]
                    R += 1
                    L = R
                elif asteroids[R-1] == -asteroids[i]:
                    # both asteroids should explode
                    R -= 1
                # else:
                    # asteroid i explodes, do nothing
                    # pass

        return asteroids[:R]