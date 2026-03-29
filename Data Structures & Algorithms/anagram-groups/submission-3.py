from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        asList = defaultdict(list)
        for string in strs:
            currentStr = [0] * 26
            for c in string:
                currentStr[ord(c) - ord('a')] += 1
            asList[tuple(currentStr)].append(string)
            
        return list(asList.values())