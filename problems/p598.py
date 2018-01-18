import unittest


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not m or not n:
            return 0
        if not ops:
            return m * n
        min_a = m
        min_b = n
        for a, b in ops:
            if a and a < min_a:
                min_a = a
            if b and b < min_b:
                min_b = b
        return min_a * min_b


class Test(unittest.TestCase):
    def test(self):
        self._test(3, 3, [[2, 2], [3, 3]], 4)
        self._test(3, 3, [], 9)
        self._test(3, 3, [[0, 0]], 9)
        self._test(3, 3, [[10, 10]], 9)
        self._test(3, 3, [[0, 0], [2, 2]], 4)

    def _test(self, m, n, ops, expected):
        actual = Solution().maxCount(m, n, ops)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
