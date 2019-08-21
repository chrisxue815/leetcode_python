import unittest
from typing import List

import utils


# O(n * m! / (m-n)!) time. O(n) space. Brute-force, backtracking, pruning, TLE.
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        min_sum = 0x7fffffff

        def permute(start, curr_sum):
            if start >= len(workers):
                nonlocal min_sum
                min_sum = min(min_sum, curr_sum)

            if curr_sum >= min_sum:
                return

            for i in range(start, len(bikes)):
                bikes[start], bikes[i] = bikes[i], bikes[start]
                s = curr_sum + abs(workers[start][0] - bikes[start][0]) + abs(workers[start][1] - bikes[start][1])
                permute(start + 1, s)
                bikes[start], bikes[i] = bikes[i], bikes[start]

        permute(0, 0)
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
