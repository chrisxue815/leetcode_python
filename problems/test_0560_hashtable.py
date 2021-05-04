import collections
import unittest
from typing import List

import utils


# O(n) time. O(n) space. Hash table, prefix sum
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        counter = collections.Counter()
        counter[0] = 1
        sum = 0

        for num in nums:
            sum += num
            result += counter[sum - k]
            counter[sum] += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
