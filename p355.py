import unittest
import collections


class User(object):
    def __init__(self):
        self.followees = set([self])
        self.tweets = collections.deque()


class Tweet(object):
    def __init__(self, id, time):
        self.id = id
        self.time = time


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users = collections.defaultdict(User)
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        tweets = self.users[userId].tweets
        if len(tweets) >= 10:
            tweets.popleft()
        tweets.append(Tweet(tweetId, self.time))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        user = self.users[userId]
        tweets = sorted(
            (tweet for followee in user.followees for tweet in followee.tweets),
            key=lambda x: x.time,
            reverse=True)
        return map(lambda x: x.id, tweets[:10])

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId == followeeId:
            return
        follower = self.users[followerId]
        followee = self.users[followeeId]
        follower.followees.add(followee)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
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
        self.assertEqual(twitter.getNewsFeed(1), [5])

        # User 2 posts a new tweet (id = 6).
        twitter.postTweet(2, 6)

        # User 1's news feed should return a list with 1 tweet id -> [5].
        self.assertEqual(twitter.getNewsFeed(1), [5])

        # User 1 follows user 2.
        twitter.follow(1, 2)

        # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
        # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
        self.assertEqual(twitter.getNewsFeed(1), [6, 5])

        # User 1 unfollows user 2.
        twitter.unfollow(1, 2)

        # User 1's news feed should return a list with 1 tweet id -> [5],
        # since user 1 is no longer following user 2.
        self.assertEqual(twitter.getNewsFeed(1), [5])


if __name__ == '__main__':
    unittest.main()
