from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        This seems a case for DP
           n e e t c o d e
             e e
        '''


        queue = deque([0]) # Possible starts
        words = set(wordDict)
        tested = set()
        while queue:
            i = queue.popleft()
            if i in tested:
                continue
            tested.add(i)
            for j in range(i+1, len(s)+1):
                if s[i:j] in words:
                    if j == len(s):
                        return True
                    queue.append(j)
        return False