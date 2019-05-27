import unittest
import bisect


class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        lo = 0

        for greed_index, greed in enumerate(g):
            lo = bisect.bisect_left(s, greed, lo)
            if lo < len(s):
                lo += 1
            else:
                return greed_index
        return len(g)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [1, 1], 1)
        self._test([1, 2], [1, 2, 3], 2)

    def _test(self, g, s, expected):
        actual = Solution().findContentChildren(g, s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
