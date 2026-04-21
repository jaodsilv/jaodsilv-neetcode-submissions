class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        generated = {}
        def backtracking(pairs, closes):
            if (pairs, closes) in generated:
                return generated[(pairs, closes)]

            if pairs == 0:
                res = {')'*closes}
                generated[(pairs, closes)] = res
                return res

            opens = {'(' + v for v in backtracking(pairs-1, closes+1)} if pairs > 0 else set()
            closing = {')' + v for v in backtracking(pairs, closes-1)} if closes > 0 else set()
            generated[(pairs, closes)] = opens | closing
            return generated[(pairs, closes)]
        return list(backtracking(n, 0))

            