import heapq

class User:
    def __init__(self, id):
        self.id = id
        self.following = {}
        # self.followees = {}
        self.tweets = []
        # self.feedCache = []

    def post(self, tweetId, timestamp):
        self.tweets.append((timestamp, tweet))

class Twitter:
    # O(1)
    def __init__(self):
        self.users = {}
        self.tweets = []
        self.time = 0

    # O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        if userId not in self.users:
            self.users[userId] = User(userId)
        user = self.users[userId]
        user.tweets.append((self.time, tweetId))
        self.time += 1

    # Aiming for O(nlogn)
    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users[userId] = User(userId)
            return []
        user = self.users[userId]
        following = user.following

        minTime = self.time
        heap = user.tweets[::-1][:10]
        heapq.heapify(heap)

        for followee in following.values():
            for tweet in followee.tweets[::-1]:
                if len(heap) >= 10 and tweet[0] < heap[0][0]:
                    break
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)

        return [x[1] for x in sorted(heap, reverse=True)]
        # for tweet in self.tweets[::-1]:
        #     if count == 0:
        #         break
        #     if tweet[0] in following or tweet[0] == userId:
        #         count -= 1
        #         res.append(tweet[1])

        return res

    # O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)

        if followerId == followeeId:
            return

        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        self.users[followerId].following[followeeId] = self.users[followeeId]

    # O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)

        if followerId == followeeId:
            return

        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        
        user = self.users[followerId]

        if followeeId in user.following:
            del user.following[followeeId]
