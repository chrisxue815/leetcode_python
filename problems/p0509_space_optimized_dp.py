import unittest
import utils


# O(n) time. O(1) space. Space-optimized DP.
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            raise ValueError('Expected n >= 0. Got n = {}'.format(n))
        elif n == 0:
            return 0
        elif n == 1:
            return 1

        a = 0
        b = 1

        for i in xrange(2, n + 1):
            a, b = b, a + b

        return b


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().fib(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
