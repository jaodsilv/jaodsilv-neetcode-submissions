import heapq
class Twitter:

    def __init__(self):
        self.users = set()
        self.timestamp = 0
        self.tweets = {}
        self.following = {}

    def _checkUser(self, userId):
        if userId not in self.users:
            self.users.add(userId)
            self.tweets[userId] = []
            self.following[userId] = {userId}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self._checkUser(userId)
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self._checkUser(userId)
        heap = []
        for id in self.following[userId]:
            for i in range(len(self.tweets[id])-1, -1, -1):
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
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self._checkUser(followerId)
        self._checkUser(followeeId)
        if followerId == followeeId:
            return

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._checkUser(followerId)
        self._checkUser(followeeId)
        if followerId == followeeId:
            return

        self.following[followerId].discard(followeeId)
        
