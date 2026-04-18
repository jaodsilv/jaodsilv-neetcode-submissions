from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        most_common = Counter(tasks).most_common()
        _, top_counter = most_common[0]
        distinct = len(most_common)
        top_extras = 0
        while top_extras < distinct and most_common[top_extras][1] == top_counter:
            top_extras += 1

        if len(tasks) > (top_counter-1) * (n + 1) + 1:
            return len(tasks)
        return (top_counter-1) * (n+1) + top_extras