class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = []
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                c = [c]
                while s[i+1].isdigit():
                    i += 1
                    c.append(s[i])
                stack.append(int(''.join(c)))
            elif c == ']':
                buf = []
                while stack[-1] != '[':
                    buf.append(stack.pop())
                stack.pop()
                s2 = ''.join(buf[::-1])
                stack[-1] = s2 * stack[-1]
            else:
                stack.append(c)
            i+=1
        return ''.join(stack)