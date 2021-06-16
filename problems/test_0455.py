import bisect
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(1) space. Sorting, binary search.
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        lo = 0

        for greed_index, greed in enumerate(g):
            lo = bisect.bisect_left(s, greed, lo)
            if lo < len(s):
                lo += 1
            else:
                return greed_index

        return len(g)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
