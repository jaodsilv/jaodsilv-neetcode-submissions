class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        if len(prices) == 2:
            return max(0, prices[1]-prices[0])
        '''
        4 actions:
        1. Buy
        2. sell
        3. Wait to Sell
        4. Wait to Buy

           [    1,       3,                  4,                  0,  4]
         B [  0-1,     0-3,                0-4,                2-0,  -]
            0-[0],   0-[1],          WB[1]-[2],          WB[2]-[3],
         S [    0,     0+2,                0+3,                -1S, 6S]
                0,B[0]+[1],max(B[1],WS[1])+[2],max(B[2],WS[2])+[3],
        WS [    0,      -1,                 -1,                 -1,  -]
                0,    B[0],    max(B[1],WS[1]),    max(B[2],WS[2]),
        WB [    0,       0,                  2,                  3,  3]
                0,   WB[0],    max(S[1],WB[1]),    max(WB[2],S[2]),
        '''
        B  = -prices[1]
        S  = prices[1]-prices[0]
        WS = -prices[0]
        WB = 0
        for i in range(2, len(prices)):
            WS= max(B, WS)
            prevWB = WB
            WB= max(S,WB)
            S = WS + prices[i]
            B = prevWB - prices[i]
        return max(S, WB)
