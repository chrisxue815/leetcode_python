import unittest
import itertools
import math


def generate_palindromes(n):
    for num_digits in xrange(n << 1, 0, -1):
        hi_i = num_digits >> 1
        lo_i = (num_digits - 1) >> 1
        p = 0
        for _ in xrange(num_digits):
            p = p * 10 + 9
        while p:
            yield p

            while True:
                hi = 10 ** hi_i
                lo = 10 ** lo_i
                digit = p % (hi * 10) // hi
                if digit:
                    p += (digit - 1) * hi - digit * hi
                    if hi != lo:
                        p += (digit - 1) * lo - digit * lo
                    hi_i = num_digits >> 1
                    lo_i = (num_digits - 1) >> 1
                    break
                else:
                    p += 9 * hi + 9 * lo
                    hi_i += 1
                    lo_i -= 1
    yield 0


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9

        hi = 10 ** n
        for p in generate_palindromes(n):
            root = int(math.sqrt(p))
            for factor in xrange(root, hi):
                q, r = divmod(p, factor)
                if not r and q < hi:
                    return p % 1337
        return 0


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 9)
        self._test(2, 987)

    def _test(self, heights, expected):
        actual = Solution().largestPalindrome(heights)
        self.assertEqual(actual, expected)

    def test_generate_palindromes(self):
        self._test_generate_palindromes(1, [
            99, 88, 77, 66, 55, 44, 33, 22, 11,
            9, 8, 7, 6, 5, 4, 3, 2, 1, 0
        ])
        self._test_generate_palindromes(3, [
            999999, 998899, 997799, 996699, 995599, 994499, 993399, 992299, 991199, 990099,
            989989, 988889, 987789, 986689, 985589, 984489, 983389, 982289, 981189, 980089,
            979979
        ])

    def _test_generate_palindromes(self, n, expected):
        actual = list(itertools.islice(generate_palindromes(n), len(expected)))
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
