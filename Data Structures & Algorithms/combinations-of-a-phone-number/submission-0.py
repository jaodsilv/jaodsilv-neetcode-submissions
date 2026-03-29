class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []
        print(digits)
        res = [[]]
        for d in digits:
            copy = []
            # print(letterMap[d])
            for c in letterMap[d]:
                for prev in res:
                    prev = prev.copy()
                    # print('prev', prev)
                    prev.append(c)
                    copy.append(prev)
                # print('res, copy', res, copy)
            res = copy
            # print('res', res)
        return [''.join(s) for s in res]