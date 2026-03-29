class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        # Make the num2 the number with less digits
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        def ctoi(c: str) -> int:
            return ord(c) - ord('0')

        def digit_sum(a: int, b: int, carry: int) -> tuple[int, int]:
            res = a + b + carry
            return (res % 10, res // 10)

        def sum(a: list, b: list) -> list[int]:
            if len(a) > len(b):
                a, b = b, a
            carry = 0
            res = []
            for i in range(len(a)):
                r, carry = digit_sum(a[i], b[i], carry)
                res.append(r)
            for i in range(len(a), len(b)):
                r, carry = digit_sum(0, b[i], carry)
                res.append(r)
            if carry:
                res.append(carry)
            print(f'a+b={a}+{b}={res}')
            return res

        results = {}
        n1 = [ctoi(c) for c in num1][::-1]
        n2 = [ctoi(c) for c in num2][::-1]

        def _multiply(d: int) -> list[int]:
            if d in results:
                return results[d]

            res = []
            carry = 0
            for n in n1:
                m = n * d + carry
                carry = m // 10
                res.append(m % 10)
            if carry:
                res.append(carry)
            results[d] = res
            return res


        tens = 1
        carry = 0
        res  = _multiply(n2[0])
        print(res)
        for i in range(1, len(num2)):
            curr = [0]*tens + _multiply(n2[i])
            print(curr)
            res = sum(res, curr)
            tens += 1
        return ''.join([str(x) for x in res[::-1]])

