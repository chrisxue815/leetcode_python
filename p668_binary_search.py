import unittest


def _count_smaller_or_equal_numbers(num, m, n):
    count = 0
    for a in xrange(1, m + 1):
        count += min(num // a, n)
    return count


# O(min(m, n) * log(mn) time. O(1) space. Binary search.
class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if m > n:
            m, n = n, m

        lo = 1
        hi = m * n

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            count = _count_smaller_or_equal_numbers(mid, m, n)
            if count < k:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


class Test(unittest.TestCase):
    def test(self):
        self._test(3, 3, 5, 3)
        self._test(3, 3, 4, 3)
        self._test(2, 3, 6, 6)
        self._test(42, 34, 401, 126)

    def _test(self, m, n, k, expected):
        actual = Solution().findKthNumber(m, n, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
