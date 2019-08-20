import unittest
from typing import List

import utils


# O(nm) time. O(nm) space. Bucket sort.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        pairs_by_distance = [[] for _ in range(2000)]

        for wi, (wx, wy) in enumerate(workers):
            for bi, (bx, by) in enumerate(bikes):
                dist = abs(wx - bx) + abs(wy - by)
                pairs_by_distance[dist].append((wi, bi))

        result = [-1] * len(workers)
        num_results = 0
        bike_free = [True] * len(bikes)

        for pairs in pairs_by_distance:
            for wi, bi in pairs:
                if result[wi] == -1 and bike_free[bi]:
                    result[wi] = bi
                    bike_free[bi] = False
                    num_results += 1

                    if num_results >= len(workers):
                        break

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
