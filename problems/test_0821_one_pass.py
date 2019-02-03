import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        distances = [0] * len(s)
        hi = s.find(c)

        for i in xrange(hi):
            distances[i] = hi - i

        while True:
            lo = hi
            hi = s.find(c, lo + 1)

            if hi == -1:
                break

            mid = lo + ((hi - lo + 1) >> 1)

            for i in xrange(lo + 1, mid):
                distances[i] = i - lo

            for i in xrange(mid, hi):
                distances[i] = hi - i

        for i in xrange(lo + 1, len(s)):
            distances[i] = i - lo

        return distances


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().shortestToChar(**vars(case.args))
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
