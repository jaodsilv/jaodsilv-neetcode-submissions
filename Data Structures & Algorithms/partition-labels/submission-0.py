class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Let's first map all character to positions
        # We have to ensure that if a character is in the first string, all repetions must be in that same string
        # So, need to actually store only the last position
        charmap = {}
        for i, c in enumerate(s):
            charmap[c] = i
        
        # Now we build those string ranges
        res = []

        # For the first character we start a new string range
        L = 0
        R = charmap[s[0]]
        # We remove to mark it was already consumed
        del charmap[s[0]]
        for i in range(1, len(s)):
            c = s[i]
            # If i is R+1, we start a new string
            if i == R + 1:
                res.append(R - L + 1)
                L = i
                R = charmap[c]
                # We remove to mark it was already consumed
                del charmap[c]
            elif c in charmap: # c was not processed yet
                if charmap[c] > R:
                    R = charmap[c]
                    # If R is the last character we don't need to continue
                    if R == len(s) - 1:
                        break
                del charmap[c]
        res.append(R - L + 1)
        return res