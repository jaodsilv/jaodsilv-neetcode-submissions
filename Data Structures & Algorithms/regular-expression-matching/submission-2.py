class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Let's truncate the exercise
        first = 0
        while first < min(len(p), len(s)) and p[first].isalpha() and (first == len(p) - 1 or p[first+1] != '*'):
            if p[first] != '.' and p[first] != s[first]:
                return False
            first += 1
        p = p[first:]
        s = s[first:]
        
        lastP = len(p) - 1
        lastS = len(s) - 1
        while lastP >= 0 and lastS >= 0 and (p[lastP].isalpha() or p[lastP] == '.'):
            if p[lastP] != '.' and p[lastP] != s[lastS]:
                return False
            lastS -= 1
            lastP -= 1
        s = s[:lastS+1]
        p = p[:lastP+1]

        if p == '.*' or (len(s) == 0 and (len(p) == 0 or (len(p) == 2 and p[1] == '*'))):
            return True
        
        tp = []
        for c in p:
            if c == '*':
                tp[-1] = tp[-1] + '*'
            else:
                tp.append(c)

        print(tp, p, s)
        dp = [False]*len(tp) + [True]
        for i in range(len(tp)-1, -1, -1):
            if len(tp[i]) == 2:
                dp[i] = True
            else:
                break
        '''
            G (. *)   y   (k *) (z*) -
        G   T   T     F     F     F  F
        x   F   T     F     F     F  F
        y   F   T     T     F     F  F
        z   F   F     F     T     T  F
        z   F   F     F     T     T  F
        -   F   F     F     F     F  T

            (n*) -
        n    T  F
        n    T  F
        n    T  F
        -    T  T
        '''
        for i in range(len(s)-1,-1,-1):
            dpPrev = dp
            dp = [False]*(len(tp)+1)
            for j in range(len(tp)-1,-1,-1):
                if tp[j] == '.*':
                    dp[j] = dp[j+1] or dpPrev[j] or dpPrev[j+1]
                elif tp[j] == '.' or tp[j] == s[i]:
                    dp[j] = dpPrev[j+1]
                elif tp[j][0] == s[i]:
                    dp[j] = dp[j+1] or dpPrev[j+1] or dpPrev[j]
                else:
                    dp[j] = dp[j+1]

        return dp[0]
                