import unittest


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        counts = [0] * (n + 1)

        for citation in citations:
            if citation >= n:
                counts[n] += 1
            else:
                counts[citation] += 1

        h = 0
        for i in xrange(n, -1, -1):
            h += counts[i]
            if h >= i:
                return i
        return 0


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 0, 6, 1, 5], 3)
        self._test([2, 1], 1)
        self._test([1, 2, 3, 4, 5], 3)
        self._test([1, 2, 3, 4, 5, 6], 3)
        self._test([1, 2, 3, 3, 4], 3)
        self._test([1, 2, 3, 3, 3, 4], 3)
        self._test([0], 0)

    def _test(self, citations, expected):
        actual = Solution().hIndex(citations)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
