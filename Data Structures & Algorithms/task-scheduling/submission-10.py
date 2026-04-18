from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0]*26
        for t in tasks:
            counter[ord(t)-ord('A')] += 1
        
        top_counter = max(counter)
        top_extras = counter.count(top_counter)

        if len(tasks) > (top_counter-1) * (n + 1) + 1:
            return len(tasks)
        return (top_counter-1) * (n+1) + top_extras