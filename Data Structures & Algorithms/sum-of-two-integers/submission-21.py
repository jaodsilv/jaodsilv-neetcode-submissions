class Solution:
    def getSum(self, a: int, b: int) -> int:
        # making a the one with the biggest abs
        if abs(a) < abs(b):
          a, b = b, a
        if b == 0:
          return a
        
        isNeg = a < 0
        if isNeg:
          a, b = -a, -b
        isSub = b < 0
        
        up = 0
        resList = []
        for i in range(11):
          resList.append((a & 1) ^ (b & 1) ^ up)
          up = ((a & up) | (b & up) | (1 & a & b))
          a >>= 1
          b >>= 1
        print(''.join([str(i) for i in resList]))
        resList.reverse()
        res = 0
        for i in resList:
          res <<= 1
          res |= i
        
        return -res if isNeg else res
        if isSub:
          b = -b

        else:
          pass

'''
  10110
 -01001 = 01101
=>10111
 -01010 = 01101
=>00101
+(10000
 -01000) = 01101
=>00101
+(11000
 -10000)
=>01101

  10000
 -01011 = 0
=>10111
 -01010 = 01101
=>00101
+(10000
 -01000) = 01101
=>00101
+(11000
 -10000)
=>01101

'''