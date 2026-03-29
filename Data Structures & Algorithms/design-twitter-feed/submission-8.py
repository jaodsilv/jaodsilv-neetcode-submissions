from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.posts = {}
        self.following = defaultdict(set) # Maps follower to followee
        self.clock = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._checkUser(userId)
        self.posts[userId].appendleft((self.clock, tweetId))
        if len(self.posts[userId]) > 10:
            self.posts[userId].pop()
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self._checkUser(userId)
        minClock = -1
        heap = list(self.posts[userId])
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


    def follow(self, followerId: int, followeeId: int) -> None:
        self._checkUser(followerId)
        if followeeId == followerId:
            return
        self._checkUser(followeeId)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        self._checkUser(followeeId)
        self._checkUser(followerId)
        
    def _checkUser(self, userId):
        if userId not in self.posts:
            self.posts[userId] = deque()
