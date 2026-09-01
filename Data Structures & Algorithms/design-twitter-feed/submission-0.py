class Twitter:

    def __init__(self):
        self.fmap = defaultdict(set) #maps who all user1 follows user:[]
        self.tweets = defaultdict(list) # it should have userId: time, tweetID
        self.currtime = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.currtime += 1
        self.tweets[userId].append((self.currtime,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.fmap[userId] # this will be a list of followees
        # get followees' tweets
        t_info = []
        ans = []
        for f in followees:
            t_info.extend(self.tweets[f]) # [[f1], [f2]]
        t_info.extend(self.tweets[userId])
        
        heapq.heapify_max(t_info)

        for _ in range(10):
            if not t_info:
                break
            ans.append(heapq.heappop_max(t_info)[1])
        
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fmap[followerId].discard(followeeId)
