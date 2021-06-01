import unittest
from typing import List

import utils


# O(len(trust) + n) time. O(n) space. Graph.
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # in-degree - out-degree
        counts = [0] * (n + 1)
        counts[0] = -2

        for a, b in trust:
            counts[a] -= 1
            counts[b] += 1

        return next((i for i, count in enumerate(counts) if count == n - 1), -1)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
