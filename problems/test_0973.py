import heapq
import unittest
from typing import List

import utils


# O(n) time. O(K) space. Heap sort.
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if K <= 0:
            return []

        q = []

        for x, y in points:
            distance_square = x * x + y * y

            if len(q) < K:
                heapq.heappush(q, (-distance_square, x, y))
            elif distance_square < -q[0][0]:
                heapq.heapreplace(q, (-distance_square, x, y))

        return [[x, y] for _, x, y in q]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().kClosest(**case.args.__dict__)
            self.assertCountEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
