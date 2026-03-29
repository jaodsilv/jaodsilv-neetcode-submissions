class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            res = t
            if t in '+-*/':
                v2 = stack.pop()
                v1 = stack.pop()
                print(f'{v1} {t} {v2}')
                if t == '+':
                    res = v1 + v2
                elif t == '-':
                    res = v1 - v2
                elif t == '*':
                    res = v1 * v2
                else:
                    res = v1 // v2
                    if res < 0 and v1 % v2 != 0:
                        res += 1
            stack.append(int(res))
            print(f'stack = {stack}')
        return stack[0]