class Solution:
    def validPalindrome(self, s: str) -> bool:
        mid = math.ceil(len(s) / 2)
        left = s[:mid]
        right = s[-mid:][::-1] # -mid compensates the case where s has odd size
        if left == right:
            return True
        
        for i in range(mid):
            if left[i] != right[i]:
                # since we can remove only one, either substring must be the same
                lremoved = left[i+1:mid] == right[i:mid-1]
                rremoved = left[i:mid-1] == right[i+1:mid]
                return lremoved or rremoved
        return True