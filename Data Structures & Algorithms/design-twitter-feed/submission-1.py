# import heapq

class User:
    def __init__(self, id):
        self.id = id
        self.following = set()
        # self.followees = {}
        self.tweets = []
        # self.feedCache = []

    def post(self, tweetId, timestamp):
        self.tweets.append((timestamp, tweet))

class Twitter:
    def __init__(self):
        self.users = {}
        self.tweets = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        if userId not in self.users:
            self.users[userId] = User(userId)
        # user = self.users[userId]
        # user.tweets.append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users[userId] = User(userId)
            return []
        following = self.users[userId].following

        count = 10
        res = []
        for tweet in self.tweets[::-1]:
            if count == 0:
                break
            if tweet[0] in following or tweet[0] == userId:
                count -= 1
                res.append(tweet[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)

        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        user = self.users[followerId]
        user.following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)

        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        
        user = self.users[followerId]
        user.following.discard(followeeId)
