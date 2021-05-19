import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Built-in sort.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])[:k]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution, check_result=self.check_result)

    def check_result(self, case, actual, msg):
        self.assertCountEqual(case.expected, actual, msg)


if __name__ == '__main__':
    unittest.main()
