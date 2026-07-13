import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.counter = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        self.follow(userId, userId)
        for user in self.following[userId]:
            userTweets = self.tweets[user]
            if userTweets:
                n = len(userTweets) - 1
                heapq.heappush(maxHeap, (-userTweets[n][0], userTweets, n))
        feed = []
        feedSize = 0
        while maxHeap and feedSize < 10:
            _, userTweets, i = heapq.heappop(maxHeap)
            feed.append(userTweets[i][1])
            if i > 0:
                heapq.heappush(maxHeap, (-userTweets[i - 1][0], userTweets, i - 1))
            feedSize += 1

        self.unfollow(userId, userId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

