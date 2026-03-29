class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if num1 == '1':
            return num2
        if num2 == '1':
            return num1
        
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        # We can decompose the num1 into multiples of 10
        list1 = list(num1[::-1])
        list2 = list(num2[::-1])

        memo = {'0': ['0']}
        def multi(a: list[str], b: str) -> list[str]: # This would run complete up to 9 times
            if b in memo:
                return memo[b]
            bnum = int(b)
            carry = 0
            res = []
            for c in a:
                num = bnum*int(c) + carry
                res.append(str(num % 10))
                carry = num // 10
            if carry > 0:
                res.append(str(carry))
            memo[b] = res
            return memo[b]

        def sum(a: list[str], b: list[str], offsetB: int) -> list[str]:
            carry = 0
            res = list(a[:offsetB])
            print(f'initialSum = {res}')
            for i in range(offsetB, min(len(a), len(b)+offsetB)):
                num = int(a[i])+int(b[i-offsetB])+carry
                if num >= 10:
                    carry = 1
                    num -= 10
                else:
                    carry = 0
                res.append(str(num))
            print(f'loop1 = {res}')
            if len(a) < len(b)+offsetB:
                for i in range(len(a)-offsetB, len(b)):
                    num = int(b[i]) + carry
                    if num > 10:
                        num -= 10
                        carry = 1
                    else:
                        carry = 0
                    res.append(str(num))
                print(f'loop2 = {res}')
            else:
                for i in range(len(b)+offsetB, len(a)):
                    num = int(a[i]) + carry
                    if num > 10:
                        num -= 10
                        carry = 1
                    else:
                        carry = 0
                    res.append(str(num))
                print(f'loop3 = {res}')
            if carry:
                res.append('1')
            print(f'final = {res}')
            return res

        zeroes = 0
        res = ['0']
        for c in list1:
            p = multi(list2, c)
            print(f'{res} + {[0]*zeroes + p} = ')
            res = sum(res, p, zeroes)
            print(f'\t\t{res}')
            zeroes += 1
        return ''.join(res[::-1])