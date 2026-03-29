class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Let's study how it develops
        f(0) = 0
        f(1) = 1
        f(10) = 1
        f(11) = 2

        f(100) = 1 = f(0) + 1
        f(101) = 2 = f(1) + 1
        f(110) = 2 = f(10) + 1
        f(111) = 3

        f(1000) = 1
        f(1001) = 2
        f(1010) = 2
        f(1011) = 3
        f(1100) = 2
        f(1101) = 3
        f(1110) = 3
        f(1111) = 4


        '''
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = [0, 1]

        # log(n)
        lastb = bin(n)

        # O(n) total as j will enter at most 
        for i in range(len(lastb) - 2): # O(log(n))
            for j in range(len(res)):
                res.append(res[j] + 1)
                if len(res) == n + 1:
                    return res
