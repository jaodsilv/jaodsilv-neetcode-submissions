class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        # How many extra hours we have after visiting each pile once:
        extra = h - len(piles)
        # This is the number or revisits koko can do, being possible to revisit the same multiple times
        # Let's sort the piles
        piles.sort(reverse=True)
        # We can attempt dividing visits to the top pile
        # If we end up with extra hours we can decrease more
        # If we end up with missing hours, the target result is between this and the previous tested result (inclusive to the previous result)

        def eat(k) -> int:
            hoursUsed = len(piles)
            for pile in piles:
                hours = math.ceil(pile / k) - 1
                if hours == 0:
                    break
                hoursUsed += hours
            return h - hoursUsed

        left = 1
        right = piles[0]
        while right - left > 1:
            k = (right + left) >> 1
            hoursLeft = eat(k)
            if hoursLeft < 0:
                left = k
            elif hoursLeft >= 0:
                right = k
        return right



            
