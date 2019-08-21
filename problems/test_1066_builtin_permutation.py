import itertools
import unittest
from typing import List

import utils


# O(n * m! / (m-n)!) time. O(n) space. Brute-force, built-in permutation, TLE.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        min_sum = 0x7fffffff
        for curr_bikes in itertools.permutations(bikes, r=len(workers)):
            s = sum(abs(wx - bx) + abs(wy - by) for (wx, wy), (bx, by) in zip(workers, curr_bikes))
            min_sum = min(min_sum, s)
        return min_sum


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().assignBikes(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
