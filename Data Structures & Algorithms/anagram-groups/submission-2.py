from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asList = defaultdict(list)
        for i in range(len(strs)):
            string = strs[i]
            currentStr = [0]*(ord('z') - ord('a') + 1)
            for c in string:
                currentStr[ord(c) - ord('a')] += 1
            currentStr = tuple(currentStr)
            asList[currentStr].append(i)
        
        return [[strs[i] for i in v] for v in asList.values()]