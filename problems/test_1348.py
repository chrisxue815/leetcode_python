import unittest
from typing import List

import sortedcontainers

import utils


class TweetCounts:

    def __init__(self):
        self.tweets = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.tweets:
            times = self.tweets[tweetName]
        else:
            self.tweets[tweetName] = times = sortedcontainers.SortedList()
        times.add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweets:
            return []

        if freq == 'minute':
            step = 60
        elif freq == 'hour':
            step = 3600
        else:
            step = 86400

        times = self.tweets[tweetName]
        index = times.bisect_left(startTime)
        endTime += 1
        result = []

        for start in range(startTime, endTime, step):
            end = min(endTime, start + step)
            count = 0
            while index < len(times):
                time = times[index]
                if time >= end:
                    break
                count += 1
                index += 1
            result.append(count)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, TweetCounts)


if __name__ == '__main__':
    unittest.main()
