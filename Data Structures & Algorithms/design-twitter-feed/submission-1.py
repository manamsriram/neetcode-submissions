class Twitter:

    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set) # maps follower -> set of followees
        self.tweetMap = defaultdict(list) # maps userId -> list of [time, tweetId] list of lists

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # it will have tweetIds we return in the end
        maxHeap = []
        # problem tells users follow themselves
        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if len(self.tweetMap[followee]) > 0:
                index = len(self.tweetMap[followee]) - 1 # get index of their most recent tweet
                time, tweetId = self.tweetMap[followee][index]
                # time to get most recent from the maxHeap, as first value acts as index
                # tweetId for result, followeeId to access their tweetMap
                # index tracks their next most recent tweet
                maxHeap.append([time, tweetId, followee, index - 1])

        heapq.heapify(maxHeap)
        while maxHeap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            # check if that followee has more tweets
            if index >= 0:
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(maxHeap, [time, tweetId, followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
