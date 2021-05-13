import unittest
from typing import List

import sortedcontainers

import utils


# O(nlog(k)) time. O(k) space. BST.
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = sortedcontainers.SortedSet(key=lambda it: nums[it])
        large = sortedcontainers.SortedSet(key=lambda it: nums[it])

        for i in range(k):
            large.add(i)
        for _ in range(k >> 1):
            small.add(large.pop(0))

        result = [float(nums[large[0]]) if k & 1 else (nums[small[-1]] + nums[large[0]]) / 2]

        for hi in range(k, len(nums)):
            old_small_len = len(small)
            small.discard(hi - k)
            if len(small) == old_small_len:
                large.remove(hi - k)

            large.add(hi)
            small.add(large.pop(0))

            while len(small) > len(large):
                large.add(small.pop(-1))

            result.append(float(nums[large[0]]) if k & 1 else (nums[small[-1]] + nums[large[0]]) / 2)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
