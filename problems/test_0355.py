import collections
import heapq
import itertools
import unittest
from typing import List


class User:
    def __init__(self):
        self.followees = {self}
        self.tweets = collections.deque()


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = collections.defaultdict(User)
        self.timer = itertools.count(step=-1)

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        tweets = self.users[userId].tweets
        if len(tweets) >= 10:
            tweets.pop()
        tweets.appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        user = self.users[userId]
        tweets = heapq.merge(*(followee.tweets for followee in user.followees))
        return [x[1] for x in itertools.islice(tweets, 10)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        follower = self.users[followerId]
        followee = self.users[followeeId]
        follower.followees.add(followee)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        follower = self.users[followerId]
        followee = self.users[followeeId]
        follower.followees.discard(followee)


class Test(unittest.TestCase):
    def test(self):
        twitter = Twitter()

        # User 1 posts a new tweet (id = 5).
        twitter.postTweet(1, 5)

        # User 1's news feed should return a list with 1 tweet id -> [5].
        self.assertEqual([5], twitter.getNewsFeed(1))

        # User 2 posts a new tweet (id = 6).
        twitter.postTweet(2, 6)

        # User 1's news feed should return a list with 1 tweet id -> [5].
        self.assertEqual([5], twitter.getNewsFeed(1))

        # User 1 follows user 2.
        twitter.follow(1, 2)

        # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
        # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])

        # User 1 unfollows user 2.
        twitter.unfollow(1, 2)

        # User 1's news feed should return a list with 1 tweet id -> [5],
        # since user 1 is no longer following user 2.
        self.assertEqual([5], twitter.getNewsFeed(1))


if __name__ == '__main__':
    unittest.main()
