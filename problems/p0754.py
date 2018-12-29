import math
import unittest
import utils


# O(1) time. O(1) space. Math.
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        n = int(math.ceil(math.sqrt(0.25 + 2 * target) - 0.5))
        if ((1 + n) * n // 2 - target) & 1:
            if n & 1:
                return n + 2
            else:
                return n + 1
        else:
            return n


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().reachNumber(case.target)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
