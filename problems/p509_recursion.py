import unittest
import utils


# O(2^n) time. O(n) space. Recursion.
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 1:
            return self.fib(n - 1) + self.fib(n - 2)
        elif n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            raise ValueError('Expected n >= 0. Got n = {}'.format(n))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p509.json').test_cases

        for case in cases:
            actual = Solution().fib(case.n)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
