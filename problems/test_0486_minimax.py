import unittest
from typing import List

import utils

DEFAULT_VALUE = 0x7fffffff


# O(n^2) time. O(n^2) space. Minimax, memorization.
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        cache = [[DEFAULT_VALUE] * (len(nums) + 1) for _ in range(len(nums) + 1)]

        for j in range(len(nums) + 1):
            cache[j][j] = 0

        def miniMax(lo, hi, is_player_1):
            if cache[lo][hi] != DEFAULT_VALUE:
                return cache[lo][hi]
            if is_player_1:
                result = max(miniMax(lo + 1, hi, not is_player_1) + nums[lo], miniMax(lo, hi - 1, not is_player_1) + nums[hi - 1])
            else:
                result = min(miniMax(lo + 1, hi, not is_player_1) - nums[lo], miniMax(lo, hi - 1, not is_player_1) - nums[hi - 1])

            cache[lo][hi] = result
            return result

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
