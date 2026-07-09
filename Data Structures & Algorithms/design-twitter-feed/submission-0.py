class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweets = self.tweets.get(userId, [])
        tweets.append([self.time, tweetId])
        self.tweets[userId] = tweets
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following.get(userId, set()).copy()
        users.add(userId)
        heap = []
        for user in users:
            for time, tweetId in self.tweets.get(user, []):
                heapq.heappush(heap, (-time, tweetId))
        res = []
        for _ in range(10):
            if heap:
                _, tweetId = heapq.heappop(heap)
                res.append(tweetId)
            else:
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        temp = self.following.get(followerId, set())
        temp.add(followeeId)
        self.following[followerId] = temp

    def unfollow(self, followerId: int, followeeId: int) -> None:
        temp = self.following.get(followerId, set())
        if followeeId in temp:
            temp.remove(followeeId)
            self.following[followerId] = temp

