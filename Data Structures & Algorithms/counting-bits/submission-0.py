class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        Let's study how it develops
        f(0) = 0
        f(1) = 0 + 1
        f(2) = 1 + c(10) = 2
        f(3) = 2 + c(11) = 4
        f(4) = 4 + c(100) = 5
        f(5) = 
        '''
        res = []
        for i in range(n + 1):
            b = bin(i)
            count = 0
            for j in b[2:]:
                if j == '1':
                    count += 1
            res.append(count)
        return res