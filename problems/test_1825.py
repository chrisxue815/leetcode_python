import collections
import unittest

import sortedcontainers

import utils


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.q = collections.deque()
        self.nums = sortedcontainers.SortedList()
        self.sum = self.first_k = self.last_k = 0

    def addElement(self, num: int) -> None:
        self.sum += num
        self.q.append(num)
        index = self.nums.bisect_left(num)
        if index < self.k:
            self.first_k += num
            if len(self.nums) >= self.k:
                self.first_k -= self.nums[self.k - 1]
        if index >= len(self.nums) + 1 - self.k:
            self.last_k += num
            if len(self.nums) >= self.k:
                self.last_k -= self.nums[-self.k]
        self.nums.add(num)
        if len(self.q) > self.m:
            num = self.q.popleft()
            self.sum -= num
            index = self.nums.index(num)
            if index < self.k:
                self.first_k -= num
                self.first_k += self.nums[self.k]
            elif index >= len(self.nums) - self.k:
                self.last_k -= num
                self.last_k += self.nums[-self.k - 1]
            self.nums.remove(num)

    def calculateMKAverage(self) -> int:
        if len(self.nums) < self.m:
            return -1
        return (self.sum - self.first_k - self.last_k) // (self.m - 2 * self.k)


class Test(unittest.TestCase):
    def test(self):
        utils.test_invocations(self, __file__, MKAverage)


if __name__ == '__main__':
    unittest.main()
