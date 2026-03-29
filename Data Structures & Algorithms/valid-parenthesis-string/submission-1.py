from collections import Counter
class Solution:
    def checkValidString(self, s: str) -> bool:
        L = R = 0
        for c in s:
            if c == '(':
                L += 1
                R += 1
            elif c == ')':
                L = max(0, L - 1)
                R -= 1
                if R < 0:
                    return False
            else:
                L = max(0, L - 1)
                R += 1
        return L == 0

        # First let's eliminate the obvious choices, i.e., all pairs of () without any * to bother
        # stack = []
        # for c in s:
        #     if c == ')':

        #         if not stack:
        #             return False
        #         if stack[-1] == '(':
        #             stack.pop()
        #         else:
        #             stack.append(c)
        #     else:
        #         stack.append(c)
        
        # # Precheck abs(number of ( - number of )) <= number of *
        # count = Counter(stack)
        # if abs(count['('] - count[')']) > count['*']:
        #     return False

        # s = ''.join(stack)
        # print(s)
        # return True

        # # Instead of a stack, what if we use a range of possibilities?
        # # When it is a ( goes + 1
        # # when it is a ) goes - 1
        # # When it is a * it wides the range by 1
        # # We may use a stack
        # def processS(i, stack):
        #     while i < len(s):
        #         c = s[i]
        #         if c == '(':
        #             stack.append('(')
        #         elif c == ')':
        #             if stack:
        #                 stack.pop()
        #             else:
        #                 return False
        #         else:
        #             # When a * appears, we may bifurcate it in 3 cases.
        #             # If it is valid for any of the 3, than it is valid
        #             # Case 1: as a '('
        #             stack.append('(')
        #             if processS(i + 1, stack.copy()):
        #                 return True
        #             stack.pop()
        #             # Case 2: as a ''
        #             if processS(i + 1, stack.copy()):
        #                 return True
        #             # Case 3: as a ')'
        #             if stack:
        #                 stack.pop()
        #             else:
        #                 return False
        #         i += 1
        #     return len(stack) == 0
        # return processS(0, [])
            