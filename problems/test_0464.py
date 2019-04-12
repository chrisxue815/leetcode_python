import unittest

import utils


# O(2^maxChoosableInteger) time. O(2^maxChoosableInteger) space. Minimax, memorization.
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        s = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if s < desiredTotal:
            return False

        if desiredTotal <= 0:
            return True

        cache = [0] * (1 << maxChoosableInteger)

        def minimax(candidates, target):
            if cache[candidates] != 0:
                return cache[candidates]

            for i in range(maxChoosableInteger):
                if candidates & (1 << i):
                    new_target = target - i - 1
                    if new_target <= 0 or minimax(candidates & (~(1 << i)), new_target) == 2:
                        cache[candidates] = 1
                        return 1

            cache[candidates] = 2
            return 2

        return minimax((1 << maxChoosableInteger) - 1, desiredTotal) == 1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().canIWin(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
