import unittest

_bad_version = 0


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version == _bad_version


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo


class Test(unittest.TestCase):
    def test(self):
        for n in xrange(1, 10):
            self._test(n)

    def _test(self, n):
        global _bad_version
        _bad_version = n
        actual = Solution().firstBadVersion(n)
        self.assertEqual(actual, n)


if __name__ == '__main__':
    unittest.main()
