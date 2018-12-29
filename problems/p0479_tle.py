import unittest
import itertools
import math


def generate_palindromes(hi):
    for hi in xrange(hi, -1, -1):
        s = str(hi)
        yield int(s + s[::-1])


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9

        hi = 10 ** n - 1

        for p in generate_palindromes(hi):
            root = int(math.sqrt(p))

            for factor in xrange(hi, root - 1, -1):
                q, r = divmod(p, factor)

                if q > hi:
                    break
                if not r:
                    return p % 1337


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 9)
        self._test(2, 987)
        self._test(3, 123)
        self._test(4, 597)
        self._test(5, 677)
        self._test(6, 1218)
        self._test(7, 877)
        self._test(8, 475)

    def _test(self, heights, expected):
        actual = Solution().largestPalindrome(heights)
        self.assertEqual(expected, actual)

    def test_generate_palindromes(self):
        self._test_generate_palindromes(9, [
            99, 88, 77, 66, 55, 44, 33, 22, 11,
            0
        ])
        self._test_generate_palindromes(999, [
            999999, 998899, 997799, 996699, 995599, 994499, 993399, 992299, 991199, 990099,
            989989, 988889, 987789, 986689, 985589, 984489, 983389, 982289, 981189, 980089,
            979979
        ])

    def _test_generate_palindromes(self, n, expected):
        actual = list(itertools.islice(generate_palindromes(n), len(expected)))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
