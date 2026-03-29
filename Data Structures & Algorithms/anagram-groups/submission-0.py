from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asList = defaultdict(list)
        for string in strs:
            currentStr = [0]*(ord('z') - ord('a') + 1)
            for c in string:
                currentStr[ord(c) - ord('a')] += 1
            currentStr = tuple(currentStr)
            asList[currentStr].append(string)
            
        return list(asList.values())