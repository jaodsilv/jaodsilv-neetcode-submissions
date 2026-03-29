from collections import defaultdict
import heapq

class Twitter:

    # O(1)
    def __init__(self):
        self.posts = {}
        self.following = defaultdict(set) # Maps follower to followee
        self.clock = 0

    # O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self._checkUser(userId)
        self.posts[userId].appendleft((self.clock, tweetId))
        if len(self.posts[userId]) > 10:
            self.posts[userId].pop()
        self.clock += 1

    # O(t*10log10)=O(t), where t = len(self.following[userId])
    def getNewsFeed(self, userId: int) -> List[int]:
        self._checkUser(userId)
        minClock = -1
        heap = []
        heapq.heapify(heap)
        for followee in self.following[userId]:
            for clock, tweet in self.posts[followee]:
                if clock < minClock:
                    break
                if len(heap) == 10:
                    heapq.heappushpop(heap, (clock, tweet))
                    minClock = max(minClock, heap[0][0])
                else:
                    heapq.heappush(heap, (clock, tweet))
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1]

    # O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self._checkUser(followerId)
        self._checkUser(followeeId)
        self.following[followerId].add(followeeId)

    # O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._checkUser(followerId)
        self._checkUser(followeeId)
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)
        
    # O(1)
    def _checkUser(self, userId):
        if userId not in self.posts:
            self.following[userId].add(userId)
            self.posts[userId] = deque()
