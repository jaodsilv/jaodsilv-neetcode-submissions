class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if c == ']' and last != '[':
                    return False
                if c == '}' and last != '{':
                    return False
                if c == ')' and last != '(':
                    return False
        return len(stack) == 0