class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        prev = 0
        prev2 = 0
        scores = []
        for op in operations:
            if op == 'C':
                score -= scores.pop()
            else:
                if op == '+':
                    scores.append(scores[-1] + scores[-2])
                elif op == 'D':
                    scores.append(scores[-1]<<1)
                else:
                    scores.append(int(op))
                score += scores[-1]
        return score