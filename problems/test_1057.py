import heapq
import unittest
from typing import List

import utils


# O(nmlog(nm)) time. O(nm) space. Heap sort, TLE.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        q = []

        for wi, (wx, wy) in enumerate(workers):
            for bi, (bx, by) in enumerate(bikes):
                heapq.heappush(q, (abs(wx - bx) + abs(wy - by), wi, bi))

        result = [0] * len(workers)
        num_results = 0
        worker_free = [True] * len(workers)
        bike_free = [True] * len(bikes)

        while num_results < len(workers):
            _, wi, bi = heapq.heappop(q)

            if worker_free[wi] and bike_free[bi]:
                result[wi] = bi
                num_results += 1
                worker_free[wi] = False
                bike_free[bi] = False

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().assignBikes(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
