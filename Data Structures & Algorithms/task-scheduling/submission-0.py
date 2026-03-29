from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def ctoi(c):
            return ord(c) - ord('A')

        # First lets count all tasks
        tasks = [(x[1], x[0]) for x in Counter(tasks).most_common()]
        heapq.heapify_max(tasks)

        print(tasks)
        # Since we want to minimize the number of cycles lets make a map of when it was the last time a task run
        lastTimeRun = [-n-2]*26

        res = 0
        while tasks:
            res += 1
            task = tasks[0]
            stack = []
            while tasks and lastTimeRun[ctoi(task[1])] >= res - n:
                stack.append(heapq.heappop_max(tasks))
                if tasks:
                    task = tasks[0]
                else:
                    task = None

            if len(tasks) == 0:
                # Should wait one round idly
                heapq.heapify_max(stack)
                tasks = stack
                continue

            if task[0] > 1:
                lastTimeRun[ctoi(task[1])] = res
                heapq.heapreplace_max(tasks, (task[0] - 1, task[1]))
            else:
                heapq.heappop_max(tasks)

            while stack:
                heapq.heappush_max(tasks, stack.pop())

        return res
        