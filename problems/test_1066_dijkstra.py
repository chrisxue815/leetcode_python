import heapq
import unittest
from typing import List

import utils


# O(?) time. O(?) space. Dijkstra, bit set.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        q = [(0, 0, 0)]
        visited = set()

        while True:
            dist, i, bike_taken = heapq.heappop(q)

            if bike_taken in visited:
                continue
            visited.add(bike_taken)

            if i >= len(workers):
                return dist

            for j in range(len(bikes)):
                if bike_taken & (1 << j) == 0:
                    d = dist + abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                    heapq.heappush(q, (d, i + 1, bike_taken | (1 << j)))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().assignBikes(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
