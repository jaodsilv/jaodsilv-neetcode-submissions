class Solution:
    def numDecodings(self, s: str) -> int:
        if s == "" or s[0] == '0':
            return 0

        if len(s) == 1:
            return 0 if s == '0' else 1

        # Let's check the existence of invalid sequences, such as '30'
        for i in range(len(s) - 1):
            if s[i] in '03456789' and s[i + 1] == '0':
                return 0

        # Backtracking the possible solutions
        # # But let's count backwards

        count = 1
        index = len(s) - 1
        last = 0

        # The result is fibonacci-like sequence of the bifurcations
        while index >= 0:
            if s[index] == '0':
                # No change to count, the previous digit is locked to it and the previous previous cant combine with the previous
                # For instance the previous is guaranteed to be 1 or 2
                index -= 3
                last = count
            elif s[index] in '3456789' or index == len(s) - 1 or (s[index] == '2' and s[index + 1] in '789'):
                index -= 1
                last = count
            else: # if s[index] == '1' or (s[index] == '2' and s[index + 1] in '123456'):
                tmp = count
                count += last
                last = tmp
                index -= 1
                
        return count
