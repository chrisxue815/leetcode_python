import unittest
import utils


# O(1) time. O(1) space. Math.
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        q, r = divmod(n - 2, 3)
        return 3 ** q * (r + 2)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p343.json').test_cases

        for case in cases:
            actual = Solution().integerBreak(case.n)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
