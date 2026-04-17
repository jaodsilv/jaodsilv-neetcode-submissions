import heapq
from collections import deque, defaultdict

class Twitter:
    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((self.timestamp, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followees = self.following[userId]
        followees.add(userId)
        for id in followees:
            for i in range(len(self.tweets[id])):
                timestamp, tweet = self.tweets[id][i]
                if len(heap) == 10:
                    if timestamp < heap[0][0]:
                        break
                    else:
                        heapq.heappushpop(heap, (timestamp, tweet))
                else:
                    heapq.heappush(heap, (timestamp, tweet))
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        res.reverse()
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        self.following[followerId].discard(followeeId)
        
