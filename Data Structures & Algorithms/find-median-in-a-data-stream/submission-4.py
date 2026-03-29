import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        heapq.heapify_max(self.left)
        self.right = []
        heapq.heapify(self.right)

    def addNum(self, num: int) -> None:
        if len(self.left) == 0:
            heapq.heappush_max(self.left, num)
            return
        if len(self.right) == 0:
            left = heapq.heappop_max(self.left)
            heapq.heappush_max(self.left, min(left, num))
            heapq.heappush(self.right, max(left, num))
            return

        print("add", num)
        if len(self.left) == len(self.right):
            # Now we have to add 1 to the left
            minRight = heapq.heappop(self.right)
            print("minRight", minRight)
            if num > minRight:
                heapq.heappush(self.right, num)
                heapq.heappush_max(self.left, minRight)
            else:
                heapq.heappush(self.right, minRight)
                heapq.heappush_max(self.left, num)
        else: # len(self.left) > len(self.right)
            # Now we have to add 1 to the right
            maxLeft = heapq.heappop_max(self.left)
            print("maxLeft", maxLeft)
            if num > maxLeft:
                heapq.heappush(self.right, num)
                heapq.heappush_max(self.left, maxLeft)
            else:
                heapq.heappush(self.right, maxLeft)
                heapq.heappush_max(self.left, num)
        print(self.left, self.right)

    def findMedian(self) -> float:
        left = heapq.heappop_max(self.left)
        heapq.heappush_max(self.left, left)
        if len(self.left) > len(self.right):
            print("len(self.left) > len(self.right)", len(self.left), len(self.right), left)
            return left
        else:
            right = heapq.heappop(self.right)
            heapq.heappush(self.right, right)
            print("len(self.left) == len(self.right)", len(self.left), len(self.right), left, right)
            return ((left + right) / 2)
        
        