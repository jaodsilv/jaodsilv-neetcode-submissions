class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        # RPN is left to right always, so let's invert tokens to use as a stack
        tokens.reverse()

        res = []
        while tokens:
            print(tokens)
            token = tokens.pop()
            while token.isnumeric() or token[1:].isnumeric():
                res.append(int(token))
                token = tokens.pop()
            print(res)
            right = res.pop()
            left = res.pop()
            tmp = 0
            if token == '+':
                tmp = left + right
                print(f"{left} + {right}")
            elif token == '-':
                tmp = left - right
                print(f"{left} - {right}")
            elif token == '/':
                tmp = left // right
                if tmp < 0 and left % right != 0:
                    tmp += 1
                print(f"{left} // {right}")
            else: # elif token == '*':
                tmp = left * right
                print(f"{left} * {right}")
            res.append(tmp)
            print(res)
        return res[0]