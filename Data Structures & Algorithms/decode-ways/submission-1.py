class Solution:
    def numDecodings(self, s: str) -> int:
        # Let's start with examples
        if len(s) == 0 or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        # If a digit is 0, it means the previous digit must be 1 or 2, otherwise it is invalid
        for i in range(len(s)):
            if s[i] == '0' and s[i - 1] != '2' and s[i - 1] != '1':
                return 0
        # Now we know it is valid

        # If a digit is 1, it may be combined with the next one
        # If a digit is 2, it may be combined with the next one if it is less than or equal to 6
        def count(s):
            if len(s) >= 1 and s[0] == '0':
                return 0

            if len(s) == 1:
                return 1

            if len(s) == 2 and s[1] == '0':
                return 1

            isLast = True
            for i in range(len(s) - 1):
                if s[i] == '1' or s[i] == '2':
                    s = s[i:]
                    isLast = False
                    break

            if isLast:
                return 1

            # If it is 1 or 2, it can pair Or not with the next one for sure it is not in [0, 1, 2]
            if s[1] in '0123456':
                return count(s[1:]) + count(s[2:])
            if s[0] == '1':
                return count(s[1:]) + count(s[2:])
            return count(s[1:])
        return count(s)