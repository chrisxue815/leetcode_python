import unittest
from typing import List

import utils


# O(n^2) time. O(n^2) space. Minimax, TLE.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def miniMax(lo, hi, is_player_1):
            if lo >= hi:
                return 0
            if is_player_1:
                return max(miniMax(lo + 1, hi, not is_player_1) + nums[lo], miniMax(lo, hi - 1, not is_player_1) + nums[hi - 1])
            else:
                return min(miniMax(lo + 1, hi, not is_player_1) - nums[lo], miniMax(lo, hi - 1, not is_player_1) - nums[hi - 1])

        return miniMax(0, len(nums), True) >= 0


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().PredictTheWinner(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
