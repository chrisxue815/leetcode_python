import unittest


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = citations[mid]
            h = n - mid
            if h > mid_val:
                lo = mid + 1
            elif h < mid_val:
                hi = mid - 1
            else:
                return h
        return n - lo


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5], 3)
        self._test([1, 2, 3, 4, 5, 6], 3)
        self._test([1, 2, 3, 3, 4], 3)
        self._test([1, 2, 3, 3, 3, 4], 3)
        self._test([0], 0)

    def _test(self, citations, expected):
        actual = Solution().hIndex(citations)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
