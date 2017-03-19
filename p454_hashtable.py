import collections
import unittest


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        counter = collections.Counter()
        count = 0
        for a in A:
            for b in B:
                counter[a + b] += 1
        for c in C:
            for d in D:
                count += counter[-c - d]
        return count


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2], [-2, -1], [-1, 2], [0, 2], 2)
        self._test([1, 2], [-2, -1], [-1, -1, 2], [0, 2, 2], 6)

    def _test(self, a, b, c, d, expected):
        actual = Solution().fourSumCount(a, b, c, d)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
