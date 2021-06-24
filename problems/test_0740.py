import collections
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Space-optimized DP.
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        num_counts = sorted(counts.items())
        prev_max = 0
        curr_max = 0
        prev_num = -1

        for num, count in num_counts:
            if prev_num == num - 1:
                new_max = max(prev_max + num * count, curr_max)
                prev_max = curr_max
                curr_max = new_max
            else:
                prev_max = curr_max
                curr_max += num * count
            prev_num = num

        return curr_max


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
