import unittest
from typing import List

import utils


# O(n) time. O(1) space. DP.
class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0] * (n + 1)

        for x in range(1, n + 1):
            counts[x] = counts[x >> 1] + (x & 1)

        return counts


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
