class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3

        # If it can be formed by merging both string ignoring the condition |n - m| <= 1 keeping the order, then it can also be formed otherwise
        # We may start with a dfs
        def dfs(i, j, s1, s2, turn, tested):
            '''
            i: represents the position in the string we need to add next, s1
            j: represents the position in the other string, s2
            '''
            k = i + j # The position in the third string
            if i == len(s1) and j == len(s2):
                print("nothing else to add", i, j, turn, tested)
                return True
            if i == len(s1):
                return False
            if j == len(s2):
                return s1[i:] == s3[k:]
            print("init", s1[i:], s2[j:], s3[k:])
            if (turn, i, j) in tested or (i < len(s1) and s1[i] != s3[k]):
                return False
            
            while i < len(s1) and s1[i] == s3[k]:
                if s2[j] == s3[k+1] and dfs(j, i + 1, s2, s1, turn ^ 1, tested):
                    print("success", i, j, turn, tested)
                    return True
                tested.add((turn, i, j))
                i += 1
                k += 1
                if (turn, i, j) in tested:
                    print("failure", i, j, turn, tested)
                    return False
            # tested.add((turn ^1, j, i))
            return False
        tested = set()
        return dfs(0, 0, s1, s2, 0, tested) or dfs(0, 0, s2, s1, 1, tested)
