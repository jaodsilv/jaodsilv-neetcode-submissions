class Solution:

    def encode(self, strs: List[str]) -> str:
        strs = ['##L' + s + 'R##' for s in strs]
        return ''.join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        if s == '##LR##':
            return [""]
        return s[3:-3].split('R####L')