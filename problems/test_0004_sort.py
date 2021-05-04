import unittest
from typing import List

import utils


# O((m+n) * log(m+n)) time. O(m+n) space. Sorting
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        length = len(merged)
        if length & 1 == 1:
            return merged[length >> 1]
        else:
            return (merged[(length >> 1) - 1] + merged[length >> 1]) / 2


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
